import json
import sys
import requests

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Comman-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    except requests.RequestException:
        sys.exit("Problem with the request")

    o = response.json()
    rate = o["bpi"]["USD"]["rate_float"]
    total_cost = rate * bitcoin

    print(f"${total_cost:,.4f}")

main()
