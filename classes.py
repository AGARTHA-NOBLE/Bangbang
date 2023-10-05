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