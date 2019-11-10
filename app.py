from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/user', methods=['POST'])
def add_user():
  return jsonify(request.json)

if __name__ == '__main__':
    app.run()