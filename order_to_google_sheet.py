import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

# Replace with your actual Google Sheet name
sheet = client.open("Orders").sheet1

print("🤖 Chatbot Order Collection\n")

# Step-by-step input
name = input("📝 Write your name: ")
address = input("🏠 Write your delivery address: ")
pincode = input("📮 Write your area pin code: ")
phone = input("📱 Write your phone number: ")

# Append data to Google Sheet
sheet.append_row([name, address, pincode, phone])

print("\n✅ Thank you, your order details have been submitted!")
