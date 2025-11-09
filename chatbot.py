import os
import json
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)
genai.configure(api_key=os.environ.get("GENAI_API_KEY"))

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    response = genai.chat(messages=[{"content": data["message"], "author": "user"}])
    return jsonify({"response": response.last})
