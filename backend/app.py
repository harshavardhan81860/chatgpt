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
    user_message = user_data.get("message", "").lower().strip()
    if user_message == "hi":
        return jsonify({"reply": "hello"})
    
    if user_message == "how are you?":
        return jsonify({"reply": "fine"})
    
    if user_message == "good morning":
        return jsonify({"reply": "good morning"})
        
    if user_message == "good morning":
        return jsonify({"reply": "good morning"})
    
    if user_message == "good evening":
        return jsonify({"reply": "good evening"})
    
    if user_message == "good night":
        return jsonify({"reply": "good night"})

    if user_message == "myself harsha":
        return jsonify({"reply": "hey harsha thats great"})
    
    if user_message == "terraform":
        return jsonify({"reply": "it is a iac tool"})
    
    if user_message == "kubernetes":
        return jsonify({"reply": "it is a container orc tool"})
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are HARSHA AI, a helpful and witty assistant built by Harsha."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    print("Server running at http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
