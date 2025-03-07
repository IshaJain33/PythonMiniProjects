import requests

def get_exchange_rate(base, target):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url).json()
    return response["rates"].get(target, "Invalid Currency")

base_currency = input("Enter base currency (e.g., USD): ").upper()
target_currency = input("Enter target currency (e.g., INR): ").upper()
amount = float(input("Enter amount: "))

rate = get_exchange_rate(base_currency, target_currency)
if rate != "Invalid Currency":
    converted_amount = amount * rate
    print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
else:
    print("Invalid currency entered.")
