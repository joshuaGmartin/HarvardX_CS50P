import requests
import sys


def main():
    # init error handle
    if len(sys.argv) < 2:
        sys.exit("Need num of ₿ arg")

    # get n
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Cannot convert num of ₿ arg to float")

    # get price
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    except requests.RequestException:
        sys.exit("API call error")

    price = float(response.json()["data"]["priceUsd"])

    print(f"The price of {n} ₿ is ${n * price:,.4f}")


main()
