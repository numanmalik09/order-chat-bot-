from flask import Flask, request, jsonify
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Setup Google Sheets credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_json = os.environ.get("GOOGLE_CREDS_JSON")
if not creds_json:
    raise ValueError("Missing GOOGLE_CREDS_JSON environment variable")

creds_dict = json.loads(creds_json)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("Orders").sheet1  # replace with your Google Sheet name

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    sender_id = data.get("sender_id")
    sheet.append_row([sender_id, user_message])
    return jsonify({"reply": "Order received. We'll contact you soon."})

@app.route("/", methods=["GET"])
def home():
    return "🤖 Chatbot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # use Render-assigned port
    app.run(host="0.0.0.0", port=port)
