
import requests
from flask import Flask, render_template
from  flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET','POST'])
def index():
    api_key = '20acf4f9f1a3d619ed2764b51dd7a2f1'
    url = 'https://api.themoviedb.org/3/search/movie?api_key=20acf4f9f1a3d619ed2764b51dd7a2f1&language=en-US&query={}&page=1&include_adult=false'
    #url = 'https://api.tmdb.org/3/discover/movie/?api_key='+api_key 
    movie_name = 'matrix'
    r = requests.get(url.format(movie_name)).json()
    return  render_template('index.html', data=r['results'])


