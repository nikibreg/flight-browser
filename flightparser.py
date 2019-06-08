import requests
import json 

def country(name):
    with open('countries.json') as file:
        countries = json.loads(file.read())
        try:
                return [code for code in countries.keys() if countries[code] == name][0]
        except:
                return "GE"

async def parse(from_country, to_country, depart_date, return_date):
        requestURL = "https://api.skypicker.com/flights?fly_from={}&fly_to={}&date_from={}&date_to={}".format(from_country, to_country, depart_date, return_date)
        print(requestURL)
        data = requests.get(requestURL)
        data = data.json()["data"]
        return data

async def getFlights(d):
        # from_country
        # to_country
        # depart_date
        # return_date
        # trip-type ----- ამ ეტაპზე უმოქმედო 
        # adults ----- ამ ეტაპზე უმოქმედო
        # children ----- ამ ეტაპზე უმოქმედო
        # class-of-travel ----- ამ ეტაპზე უმოქმედო
        # airline-name ----- ამ ეტაპზე უმოქმედო

        # changing country names to country keys 
        d['from_country'] = country(d['from_country'])
        d['to_country'] = country(d['to_country']) 
        # changing date format to match API requirements
        d['depart_date'] = d['depart_date'].split("-")
        d['depart_date'].reverse()
        d['return_date'] = d['return_date'].split("-")
        d['return_date'].reverse()
        d['depart_date'] = "/".join(d['depart_date']) 
        d['return_date'] = "/".join(d['return_date'])
        return await parse(d['from_country'], d['to_country'], d['depart_date'], d['return_date'])
