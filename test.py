from flask import Flask
from flask_cors import CORS, cross_origin
test = Flask(__name__)
cors = CORS(app)
test.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"
