from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})  

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route('/')
def home():
    return jsonify(message="Welcome to My app!")

@app.route('/api/test', methods=['GET'])
def test_route():
    return jsonify(message="Backend is connected!")

if __name__ == '__main__':
    app.run(debug=False, port=5000)