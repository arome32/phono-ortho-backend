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
    print('here')
    file = open('/tmp/pathname.csv','w+')
    file.write(',ORTHO TARGET,PRODUCTION,T/F')
    count = 0
    print('here')
    for word in words:
        boolVal = (words[word]['word'] == words[word]['spelled'])
        file.write(str(count) + ',' + words[word]['word'] + ',' + words[word]['spelled'] + ',' + str(boolVal) +',')
        count += 1
    file.close()
    print('finished 1')
    file = open('/tmp/pathname.csv','r+')
    print(file)
    for line in file:
        print(line)
    print('finished 2')



if __name__ == '__main__':
    app.run()