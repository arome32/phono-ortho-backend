from flask import Flask, jsonify, request

app = Flask(__name__)

users = [ 
  {'name' : 'user1'},
  {'name' : 'user2'}, 
  {'name' : 'user3'}, 
  {'name' : 'user4'} 
]

@app.route('/users')
def get_users():
  return jsonify({'users': users })

@app.route('/user', methods=['POST'])
def add_user():
  new_user = request.json
  users.append(new_user)
  return jsonify(users)

app.run(port=5000)