import flask
import time
import json
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
pool = ThreadPoolExecutor()


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
  res_file = pool.submit(result_file)
  res_db = pool.submit(result_db)
  res_api = pool.submit(result_api)

  return json.dumps({
    'file': res_file.result(),
    'db': res_db.result(),
    'api': res_api.result(),
  })


if __name__ == '__main__':
  app.run()
