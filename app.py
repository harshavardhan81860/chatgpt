from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Explicitly allow the origin where your HTML is running
CORS(app) 

def get_bot_response(user_text):
    user_text = str(user_text).lower()
    if "hi" in user_text or "hello" in user_text:
        return "Hi there! How are you doing today?"
    return "I hear you! Tell me more."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        print(f"DEBUG: Received data -> {data}") # Look for this in your terminal!
        
        user_message = data.get("message", "")
        bot_reply = get_bot_response(user_message)
        
        return jsonify({"response": bot_reply})
    except Exception as e:
        print(f"!!! CRASH ERROR: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure it's running on port 5000
    app.run(debug=True, port=5000)
