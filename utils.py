import json

def bid_ask_unpack(pricebook):
        level1 = json.loads(pricebook)
        level2 = level1["pricebooks"]
        level3 = level2[0]
        bidpricesize = level3["bids"]
        askpricesize = level3["asks"]
        b = bidpricesize[0]["price"]
        bid = float(b)
        a = askpricesize[0]["price"]
        ask = float(a)
        return bid, ask