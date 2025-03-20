from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

uri = os.getenv('MONGODB_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
collection = db['flask- mongodb-assignment']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name')
        password = request.form.get('password')

        data = {
            'name': name,
            'password': password
        }
        collection.insert_one(data)
        return 'Data submitted successfully'
    except Exception as e:
        return render_template('index.html', error_message=str(e))    

@app.route('/view')
def view():
    data = collection.find()

    data = list(data)

    for item in data:
        print(item)

        del item['_id']
    
    data = {
        'data': data
    }

    return data

if __name__ == '__main__':
    app.run(debug=True)