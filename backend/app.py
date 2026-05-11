from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Crucial: Allows port 8000 to talk to port 5000

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    # Check if 'message' exists to prevent a 500 crash
    user_text = data.get("message", "").lower()
    
    if "hi" in user_text or "hello" in user_text:
        reply = "Hello! I am your AI assistant. How can I help you today?"
    
    # 2. Status response
    elif "how are you" in user_text:
        reply = "I'm doing great, thank you for asking! I'm ready to chat."
    
    # 3. Name/Identity response
    elif "your name" in user_text:
        reply = "My name is HARSHA AI. I was built to help you learn coding!"
    
    # 4. Capability response
    elif "what can you do" in user_text:
        reply = "I can chat with you, repeat your messages, and show you how Flask and React work together."
    
    # 5. Goodbye response
    elif "bye" in user_text or "goodbye" in user_text:
        reply = "Goodbye! Have a wonderful day. Come back soon!"
        
    else:
        reply = "I received your message: " + user_text
        
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
