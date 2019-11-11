from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
@cross_origin()
def hello():
    return "Hello World!"


@app.route('/<name>')
@cross_origin()
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/user', methods=['POST'])
@cross_origin()
def add_user():
  new_user = request.json
  return jsonify(new_user)

if __name__ == '__main__':
    app.run()