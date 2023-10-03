import http.client
import json
import time
import hmac
import hashlib
import keys
from classes import Asset, Request

def authorizedRequest(request):
    timestamp = int(time.time())
    conn = http.client.HTTPSConnection("api.coinbase.com")
    payload = ''
    presig = str(timestamp) + request.method + request.requestPath
    signature = hmac.new(
        bytes(keys.coinbase_api_secret, "latin-1"),
        bytes(presig, "latin-1"),
        hashlib.sha256,
    ).hexdigest()
    headers = {
    'Content-Type':'application/json',
    "CB-ACCESS-KEY":keys.coinbase_api_key,   # API key as a string
    "CB-ACCESS-SIGN":signature,      # base64-encoded signature
    "CB-ACCESS-TIMESTAMP":timestamp  # Timestamp for your request
   }
    conn.request(request.method, request.requestPath, payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data

def getAllProducts():
    # Get a list of all market offerings.
    newReq = Request("GET", "/api/v3/brokerage/products", None)
    result = authorizedRequest(newReq)
    print(result.decode("utf-8"))


def currentAccountBalance():
    # Get a list of all wallets (accounts) for the currently authorized user.
    newReq = Request("GET", "/api/v3/brokerage/accounts/", None, None)
    result = authorizedRequest(newReq)
    print(result.decode("utf-8"))

def currentAssetPrice(assetPair):
    # Get the current price for the provided asset pair.
    newReq = Request("GET", "/api/v3/brokerage/products" + assetPair + "ticker", None, None)
    result = authorizedRequest(newReq)
    print(result.decode("utf-8"))


def spawnTx(order_id, product_name, transaction_type):
    payload = json.dumps({
    "side": transaction_type,
    "client_order_id": order_id,
    "product_id": product_name 
    })    
    newReq = Request("POST", "/api/v3/brokerage/orders", payload, None)
    result = authorizedRequest(newReq)
    print(result.decode("utf-8"))

def monitorPair(assetPair):
    pass


def main():

    order_id = 0

    coinbase_test_rest_api = "https://api-public.sandbox.exchange.coinbase.com"
    coinbase_rest_api = "https://api.coinbase.com" 


if __name__ == "__main__":
    main()