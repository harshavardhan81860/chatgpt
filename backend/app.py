from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple logic for the bot's responses
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

@app.route("/")
def home():
    return "<h1>Chatbot Server is Running</h1><p>Send a POST request to /chat to talk!</p>"

@app.route("/chat", methods=["POST"])
def chat():
    # Get the message from the JSON request
    data = request.json
    user_message = data.get("message", "")
    
    # Generate response
    bot_message = get_bot_response(user_message)
    
    return jsonify({"response": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
