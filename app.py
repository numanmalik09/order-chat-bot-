from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def verify_webhook():
    if request.method == "GET":
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if verify_token == "chatbotcrafter123":
            return challenge, 200
        return "Invalid verification token", 403
    elif request.method == "POST":
        data = request.get_json()
        print("📩 Incoming:", data)
        return "EVENT_RECEIVED", 200

@app.route("/", methods=["GET"])
def home():
    return "🤖 Chatbot is running!", 200
