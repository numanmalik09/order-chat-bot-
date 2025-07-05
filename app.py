from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Orders").sheet1

# Product catalog
products = {
    "1": {"name": "Keychain", "price": 69},
    "2": {"name": "Wooden Clock", "price": 1099}
}

# Endpoint to handle order requests
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("user_input", "").lower()

    if "order" in user_input:
        product_id = "1" if "keychain" in user_input else "2" if "clock" in user_input else None
        if product_id:
            product = products[product_id]
            # Add order to Google Sheet
            sheet.append_row([product["name"], product["price"]])
            return jsonify({"reply": f"✅ Order placed for {product['name']} - ₹{product['price']}!"})
        else:
            return jsonify({"reply": "❌ Sorry, we couldn't find that product. Please try again."})
    else:
        return jsonify({"reply": "👋 Hi! To place an order, type: 'order keychain' or 'order clock'."})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
