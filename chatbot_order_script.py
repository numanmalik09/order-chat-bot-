import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Orders").sheet1

# Product catalog
products = {
    "1": {"name": "Keychain", "price": 69},
    "2": {"name": "Wooden Clock", "price": 1099}
}

# Bot starts
def chatbot():
    print("🤖 Welcome to the Order Bot!")
    user_input = input("👋 Say hi to begin (hi, hello, hlo, i want one order): ").lower()

    if user_input in  ["hi", "hello", "hlo", "i want one order", "order"]:
        print("\n🔘 Options:")
        print("1. Order")
        print("2. Track Order")
        option = input("👉 Choose option (1 or 2): ")

        if option == "1":
            print("\n🛍 Products Available:")
            for pid, info in products.items():
                print(f"{pid}. {info['name']} - {info['price']}")

            choice = input("👉 Enter the product number: ")
            product = products.get(choice)

            if product:
                print(f"💵 Price of {product['name']}: {product['price']}")
                confirm = input("📦 Do you want to order this product? (yes/no): ").lower()
                if confirm == "yes":
                    customization = input("🎨 Any customization? (Type 'no' if none): ")

                    print("\n📮 Please provide your delivery details:")
                    name = input("✍️ Name: ")
                    address = input("🏡 Address: ")
                    pincode = input("📍 Pincode: ")
                    phone = input("📞 Phone Number: ")

                    # Save to Google Sheet
                    sheet.append_row([
                        name, address, pincode, phone,
                        product['name'], product['price'], customization
                    ])
                    print("\n✅ Thank you so much, your order will be delivered in a week.")
                else:
                    print("👍 Okay! You can order anytime by saying hi.")
            else:
                print("❌ Invalid product selected.")
        elif option == "2":
            print("🔍 To track your order, please contact us on Instagram or WhatsApp.")
        else:
            print("❌ Invalid option. Please start again.")
    else:
        print("⚠️ Start from beginning by saying hi, hello, or order.")

if __name__ == "__main__":
    chatbot()
