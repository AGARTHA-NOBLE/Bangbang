import http.client
import json
import time
import hmac
import hashlib

import keys
from classes import Request

def authorizedRESTRequest(request):
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
    result = authorizedRESTRequest(newReq)
    print(result.decode("utf-8"))

def getUserAuth():
    newReq = Request("GET", "/user/auth", '', '')
    result = authorizedRESTRequest(newReq)
    print(result.decode("utf-8"))


def getAllProducts():
    # Get a list of all market offerings.
    newReq = Request("GET", "/api/v3/brokerage/products", '', '')
    result = authorizedRESTRequest(newReq)
    return(result.decode("utf-8"))


def currentAccountBalance():
    # Get a list of all wallets (accounts) for the currently authorized user.
    newReq = Request("GET", "/api/v3/brokerage/accounts", '', '')
    result = authorizedRESTRequest(newReq)
    print(result.decode("utf-8"))

def bidAskTest():
    newReq = Request("GET", "/api/v3/brokerage/best_bid_ask", '', '')
    result = authorizedRESTRequest(newReq)
    print(result.decode("utf-8"))


def currentAssetPrice(assetPair):
    # Get the current price for the provided asset pair.
    queryParams = "?product_ids=" + assetPair
    newReq = Request("GET", "/api/v3/brokerage/best_bid_ask", '', queryParams)
    result = authorizedRESTRequest(newReq)
    print(result.decode("utf-8"))


def spawnTx(order_id, product_name, transaction_type):
    payload = json.dumps({
    "side": transaction_type,
    "client_order_id": order_id,
    "product_id": product_name 
    })    
    newReq = Request("POST", "/api/v3/brokerage/orders", payload, None)
    result = authorizedRESTRequest(newReq)
    print(result.decode("utf-8"))