
import requests
from flask import Flask, render_template
from  flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    api_key = '20acf4f9f1a3d619ed2764b51dd7a2f1'
    url = 'https://api.tmdb.org/3/discover/movie/?api_key='+api_key 
    r = requests.get(url).json()
    return  render_template('index.html', data=r['results'])


