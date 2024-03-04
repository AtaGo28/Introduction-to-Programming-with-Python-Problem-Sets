import requests as req
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

response = req.get("https://api.coindesk.com/v1/bpi/currentprice.json")

try:
    btcpi = response.json()
    rate = btcpi["bpi"]["USD"]["rate_float"]
    amount = rate * float(sys.argv[1])
    print(f"${amount:,.4f}")
except req.RequestException:
    sys.exit("Try Again")
except ValueError:
    sys.exit("Command-line argument is not a number")
