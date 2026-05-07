import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()   


app = Flask(__name__, static_folder='../') 
CORS(app)


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def index():
    return send_from_directory('../', 'index.html')

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('../', path)

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    user_message = user_data.get("message", "").lower().strip().replace("?", "")

    print("User:", user_message)

    if not user_message:
        return jsonify({"reply": "Please type something."})

    if "how are you" in user_message:
        return jsonify({"reply": "I'm doing great, Harsha! Ready to build some infrastructure."})
    
    if user_message in ["hi", "hello", "hey"]:
        return jsonify({"reply": "Hello! How can HARSHA AI help you today?"})
    
    if "good morning" in user_message:
        return jsonify({"reply": "Good morning! Time to automate the world."})

    if "terraform" in user_message:
        return jsonify({"reply": "Terraform is an Infrastructure as Code (IaC) tool by HashiCorp."})
    
    if "kubernetes" in user_message or "k8s" in user_message:
        return jsonify({"reply": "Kubernetes is a powerful container orchestration tool."})
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are HARSHA AI, a helpful and witty assistant built by Harsha."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})
    except Exception as e:
        print("ERROR:", str(e))   
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    print("Server running at http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
