import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='../') 
CORS(app)

@app.route('/')
def index():
    return send_from_directory('../', 'index.html')

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('../', path)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_data = request.json
        if not user_data:
            return jsonify({"reply": "I didn't receive any data!"}), 400
            
        user_message = user_data.get("message", "").lower().strip()
        print(f"Server received: {user_message}")

        # Simple logic
        if user_message in ["hi", "hello", "hey"]:
            return jsonify({"reply": "Hello! I am HARSHA AI. Script mode is active."})
        
        if "terraform" in user_message:
            return jsonify({"reply": "Terraform is great for IaC!"})

        return jsonify({"reply": f"I heard you say: {user_message}"})

    except Exception as e:
        print(f"CRASH ERROR: {e}") # Look at your terminal for this!
        return jsonify({"reply": f"System Crash: {str(e)}"}), 500
