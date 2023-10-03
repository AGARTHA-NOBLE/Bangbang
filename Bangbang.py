import http.client
import json
import time
import keys
from coinbase.wallet.client import Client

# API secret FCXJGm8k998SGEN06yqgY7IkNW4szhBw 
# API key rU0r7y4VqJnk4UfF


def currentAccountBalance():
    conn = http.client.HTTPSConnection("api.coinbase.com")
    payload = ''
    headers = {
    'Content-Type': 'application/json'
    }
    conn.request("GET", "/api/v3/brokerage/accounts/" + coinbase_user_UUID, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def currentDogePrice():
    pass

def spawnTx(order_id, product_name, transaction_type):
    timestamp = time()
    signature = str(timestamp) + "POST" + "/api/v3/brokerage/orders"
    headers = {
    'Content-Type':'application/json',
    "CB-ACCESS-KEY":coinbase_API_key,   # API key as a string
    "CB-ACCESS-SIGN":signature,      # base64-encoded signature (see Signing a Message)
    "CB-ACCESS-TIMESTAMP":timestamp  # Timestamp for your request
   }
    conn = http.client.HTTPSConnection("api.coinbase.com")
    payload = json.dumps({
    "side": transaction_type,
    "client_order_id": order_id,
    "product_id": product_name 
    })
    conn.request("POST", "/api/v3/brokerage/orders", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def main():

    order_id = 0
    coinbase_API_key = keys.coinbase_api_key
    coinbase_API_secret = keys.coinbase_api_secret
    coinbase_user_UUID = 

    buy_limit = 0.07
    sell_limit = 0.10

    coinbase_test_rest_api = "https://api-public.sandbox.exchange.coinbase.com"
    coinbase_rest_api = "" 


if __name__ == "__main__":
    main()