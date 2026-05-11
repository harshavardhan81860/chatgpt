from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Crucial: Allows port 8000 to talk to port 5000

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    # Check if 'message' exists to prevent a 500 crash
    user_text = data.get("message", "").lower()
    
    if "hi" in user_text:
        reply = "Hello! I am your AI assistant."
    else:
        reply = "I received your message: " + user_text
        
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
