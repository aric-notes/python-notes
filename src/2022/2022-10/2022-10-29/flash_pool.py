import flask
import time
import json

app = flask.Flask(__name__)


def result_file():
  time.sleep(0.1)
  return 'file'


def result_db():
  time.sleep(0.2)
  return 'db'


def result_api():
  time.sleep(0.3)
  return 'api'


@app.route('/')
def index():
  res_file = result_file()
  res_db = result_db()
  res_api = result_api()

  return json.dumps({
    'file': res_file,
    'db': res_db,
    'api': res_api,
  })


if __name__ == '__main__':
  app.run()
