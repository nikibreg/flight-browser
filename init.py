from quart import Quart, websocket, request, jsonify, render_template, redirect, url_for
from flightparser import getFlights
import datetime

app = Quart('app', template_folder='templates')

async def result(flights):
    return await render_template('result.html', flights=flights, len=len, datetime=datetime)


@app.route('/', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
async def search():
    if request.method == 'GET':
        return await render_template('search.html')
    elif request.method == 'POST':
        form = await request.form
        fields = [k for k in form]                                      
        values = [form[k] for k in form]
        data = dict(zip(fields, values))
        flights = await getFlights(data)
        return await result(flights)

# app.run()