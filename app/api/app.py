from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
# Use environment variable or replace with your key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyCqbQ8T5lWKo82gSPaH3wKjDnIYXSVemG0')
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /get route to handle POST requests
@app.route("/get", methods=["POST"])
def get_response():
    try:
        # Get the message from the POST request
        data = request.get_json()
        message = data.get("message")
        
        print(f"📩 Received message: {message}")  # Debug log
        
        if not message:
            return jsonify({"response": "No message provided"}), 400
        
        # Send the message to Gemini's API and receive the response
        print("🤖 Sending to Gemini...")  # Debug log
        response = model.generate_content(message)
        
        print(f"✅ Response received: {response.text[:100]}...")  # Debug log
        
        if response.text:
            return jsonify({
                "response": response.text
            })
        else:
            return jsonify({"response": "Failed to generate response!"}), 500
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")  # Debug log
        return jsonify({
            "response": f"Error: {str(e)}"
        }), 500

if __name__ == '__main__':
    print("🚀 Starting Flask server...")
    print(f"🔑 API Key configured: {'Yes' if GEMINI_API_KEY != 'YOUR_GEMINI_API_KEY' else 'NO - Please add your key!'}")
    app.run(debug=True)