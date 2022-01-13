import os
import requests
import logging
import logging.config
from flask import Flask, render_template, request
from elasticapm.contrib.flask import ElasticAPM
from pythonjsonlogger import jsonlogger
from datetime import datetime

class ElkJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(ElkJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['@timestamp'] = datetime.now().isoformat()
        log_record['level'] = record.levelname
        log_record['logger'] = record.name

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("MainLogger")

app = Flask(__name__)
#app.config['DEBUG'] = True

app.config['ELASTIC_APM'] = {
          'SERVICE_NAME': 'FlaskApp',
          'SECRET_TOKEN': '',         
          'SERVER_URL': 'http://localhost:8200'
}
apm = ElasticAPM(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET','POST'])
def index():
    app.logger.debug("debug")
    app.logger.info("info")
    app.logger.warning("warning")
    app.logger.error("error")
    app.logger.critical("critical")
    # api_key =  os.getenv('SECRET_KEY')
    api_key =  '20acf4f9f1a3d619ed2764b51dd7a2f1'
    if request.method == 'POST' :
        movie_name = request.form.get('movie_name')
        if movie_name:
             url = 'https://api.themoviedb.org/3/search/movie?api_key={}'.format(api_key) +'&language=en-US&query={}&page=1&include_adult=false'
             r = requests.get(url.format(movie_name)).json()
        else:
          url = 'https://api.themoviedb.org/3/movie/popular?api_key={}'.format(api_key) +'&language=en-US&page=1'
          r = requests.get(url).json()
    else:
      url = 'https://api.themoviedb.org/3/movie/popular?api_key={}'.format(api_key) +'&language=en-US&page=1'
      r = requests.get(url).json()
    if not r['results']:
      return render_template('404.html'), 404
    else:
     return  render_template('index.html', data=r['results'])


if __name__ == '__main__':   
 app.run(host='0.0.0.0', port=5000)
