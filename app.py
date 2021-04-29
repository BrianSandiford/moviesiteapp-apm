
import requests
from flask import Flask, render_template, request
from  flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET','POST'])
def index():
    api_key = '20acf4f9f1a3d619ed2764b51dd7a2f1'
    if request.method == 'POST' :
        movie_name = request.form.get('movie_name')
        url = 'https://api.themoviedb.org/3/search/movie?api_key={}'.format(api_key) +'&language=en-US&query={}&page=1&include_adult=false'
        r = requests.get(url.format(movie_name)).json()
    elif request.method == 'GET' :
      url = 'https://api.themoviedb.org/3/movie/popular?api_key={}'.format(api_key) +'&language=en-US&page=1'
      r = requests.get(url).json()
    return  render_template('index.html', data=r['results'])


