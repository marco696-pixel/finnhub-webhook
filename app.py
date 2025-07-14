from flask import Flask, request

app = Flask(__name__)

FINNHUB_SECRET = "d1posk1r01qrc6gvgbq0"  # Replace with your actual secret

@app.route('/')
def home():
    return "Webhook is live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get("X-Finnhub-Secret") != FINNHUB_SECRET:
        return "Forbidden", 403
    data = request.json
    print("Received from Finnhub:", data)
    return '', 200
