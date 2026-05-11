from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- Ensure this is installed: pip install flask-cors

app = Flask(__name__)
CORS(app) # This allows your React frontend to talk to this backend

def get_bot_response(user_text):
    user_text = user_text.lower()
    if "hi" in user_text or "hello" in user_text:
        return "Hi there! How are you doing today?"
    elif "how are you" in user_text:
        return "I'm doing great, thanks for asking! How about you?"
    elif "fine" in user_text or "good" in user_text:
        return "That's awesome to hear!"
    else:
        return "That's interesting! Tell me more."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        if not data or "message" not in data:
            return jsonify({"error": "No message provided"}), 400
            
        user_message = data.get("message", "")
        bot_message = get_bot_response(user_message)
        
        return jsonify({"response": bot_message})
    except Exception as e:
        print(f"Error: {e}") # This will show the error in your terminal
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
