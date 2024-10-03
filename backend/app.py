from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://mongo:27017/")
db = client['userdb']
collection = db['users']

@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        "name": request.form['name'],
        "cnic": request.form['cnic'],
        "phone": request.form['phone'],
        "email": request.form['email']
    }
    
    # Insert into MongoDB
    collection.insert_one(user_data)
    
    return jsonify({"message": "User data saved!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
