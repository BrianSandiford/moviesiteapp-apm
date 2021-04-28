from datetime import datetime
#from flask_moment import Moment
import time
import requests
from flask import Flask, render_template
from  flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True


#@app.context_processor
@app.route('/')
def index():
    url = 'http://worldtimeapi.org/api/timezone/America/{}'
    city = 'Phoenix'
    r = requests.get(url.format(city)).json()
    # print(r)
    date_time = r['datetime']
    #offset = r['utc_offs
    now = datetime.fromisoformat(date_time)
    current_time=now.strftime("%H:%M:%S")
    print(date_time)
    print(now)
    print(current_time)
    return  render_template('index.html', current_time=current_time)