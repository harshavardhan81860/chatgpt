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
    # 1. Get user input
    user_data = request.json
    user_message = user_data.get("message", "").lower().strip().replace("?", "").replace("!", "")

    print(f"User sent: {user_message}")

    # 2. Logic for 5 specific messages
    if not user_message:
        return jsonify({"reply": "Please type something!"})

    if user_message in ["hi", "hello", "hey"]:
        return jsonify({"reply": "Hello! I am HARSHA AI. How can I help you today?"})

    if "how are you" in user_message:
        return jsonify({"reply": "I'm running smoothly! Ready to help you with your code."})

    if "terraform" in user_message:
        return jsonify({"reply": "Terraform is great! It's used for Infrastructure as Code (IaC)."})

    if "kubernetes" in user_message or "k8s" in user_message:
        return jsonify({"reply": "Kubernetes is a beast for container orchestration!"})

    if "bye" in user_message or "exit" in user_message:
        return jsonify({"reply": "Goodbye, Harsha! See you in the next deployment."})

    # 3. Fallback if none of the above 5 match
    return jsonify({"reply": "I'm currently in 'Script Mode'. I only know about: Hi, How are you, Terraform, K8s, and Bye."})

if __name__ == '__main__':
    print("Local Server running at http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
