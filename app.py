from datetime import datetime
import time
import requests
from flask import Flask, render_template
from  flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    url = 'http://worldtimeapi.org/api/timezone/America/{}'
    city = 'Phoenix'
    r = requests.get(url.format(city)).json()
    # print(r)
    date_time = r['datetime']
    offset = r['utc_offset']
    now = datetime.fromisoformat(date_time)
    print(date_time)
    print(now)
    return "Hello World"