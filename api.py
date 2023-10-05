import http.client
import json
import time
import hmac
import hashlib

import keys
from classes import Request

def authorized_REST_request(request):
    conn = http.client.HTTPSConnection("api.coinbase.com")
    timestamp = int(time.time())
    presig = str(timestamp) + request.method + request.requestPath
    signature = hmac.new(
        bytes(keys.coinbase_api_secret, "latin-1"),
        bytes(presig, "latin-1"),
        hashlib.sha256,
    ).hexdigest()
    headers = {
    'Content-Type':'application/json',
    'User-Agent':'BANGBANGv0.1',
    "CB-ACCESS-KEY":keys.coinbase_api_key,   # API key as a string
    "CB-ACCESS-SIGN":signature,      # base64-encoded signature
    "CB-ACCESS-TIMESTAMP":timestamp  # Timestamp for your request
   }
    conn.request(request.method, request.requestPath + request.queryParams, request.payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data

def getUserAccounts():
    newReq = Request("GET", "/v3/brokerage/accounts", '', '')
    result = authorized_REST_request(newReq)
    print(result.decode("utf-8"))

def getUserAuth():
    newReq = Request("GET", "/user/auth", '', '')
    result = authorized_REST_request(newReq)
    print(result.decode("utf-8"))


def get_all_products():
    # Get a list of all market offerings.
    newReq = Request("GET", "/api/v3/brokerage/products", '', '')
    result = authorized_REST_request(newReq)
    return(result.decode("utf-8"))


def current_account_balance():
    # Get a list of all wallets (accounts) for the currently authorized user.
    newReq = Request("GET", "/api/v3/brokerage/accounts", '', '')
    result = authorized_REST_request(newReq)
    print(result.decode("utf-8"))

def bid_ask_test():
    newReq = Request("GET", "/api/v3/brokerage/best_bid_ask", '', '')
    result = authorized_REST_request(newReq)
    print(result.decode("utf-8"))


def best_asset_price(assetPair):
    # Get the current price for the provided asset pair.
    queryParams = "?product_ids=" + assetPair
    newReq = Request("GET", "/api/v3/brokerage/best_bid_ask", '', queryParams)
    result = authorized_REST_request(newReq)
    return(result.decode("utf-8"))


def spawnTx(order):
    payload = json.dumps({
    "side": order.transaction_type,
    "client_order_id": order.order_id,
    "product_id": order.product_name 
    })    
    newReq = Request("POST", "/api/v3/brokerage/orders", payload, None)
    result = authorized_REST_request(newReq)
    print(result.decode("utf-8"))