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
    user_message = user_data.get("message", "")
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
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    print("Server running at http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
