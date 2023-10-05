import time
class Asset:
    def __init__(self, assetName, lowPrice, highPrice) -> None:
        self.assetName = assetName
        self.lowPrice = lowPrice
        self.highPrice = highPrice
        self.costBasis = 0 
    def calculateCostBasis():
        pass


class Request:
    def __init__(self, method, requestPath, payload, queryParams) -> None:
        self.method = method
        self.requestPath = requestPath
        self.payload = payload
        self.queryParams = queryParams

class Order:
    def __init__(self, order_id, product_name, transaction_type):
        self.order_id = order_id 
        self.product_name =  product_name
        self.transaction_type = transaction_type
        self.price_limit = 0
        self.timeout = 0 # About 30 minutes from order creation timeout for a request to timeout. 