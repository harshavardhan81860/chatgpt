import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client (Replace 'your-api-key-here' with your actual key)
client = OpenAI(api_key=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)

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    user_message = user_data.get("message", "")

    try:
        # Calling the Real AI Model
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        
        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "I'm having trouble thinking right now. Check your API key!"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
