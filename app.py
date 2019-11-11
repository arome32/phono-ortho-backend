from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello():
    return jsonify({ 'hello': 'Hello World!' })


@app.route('/<name>')
def hello_name(name):
    return jsonify({ 'name': name })

@app.route('/user', methods=['POST'])
def add_user():
  new_user = request.json
  create_csv(new_user['words'])
  return jsonify(new_user)

def create_csv(words):
    file = open('pathname.csv','rw+')
    file.write(',ORTHO TARGET,PRODUCTION,T/F')
    count = 0
    for word in words:
        print(count + ',' + word.word + ',' + word.spelled + ',' + (word.word == word.spelled) +',')
        file.write(count + ',' + word.word + ',' + word.spelled + ',' + (word.word == word.spelled) +',')
        count += 1

if __name__ == '__main__':
    app.run()