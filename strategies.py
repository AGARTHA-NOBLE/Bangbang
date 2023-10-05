from api import *
from classes import Asset
from utils import *

def Bangbang(asset):
    i = 0
    while True:
        result = best_asset_price(asset.assetName)
        bid, ask = bid_ask_unpack(result)
        print("Bid: ", bid, " Ask: ", ask)
        if bid < asset.lowPrice:
            # Buy if coin is below minimum price boundary.
            print("Price below target. Purchasing.")
        elif ask > asset.highPrice:
            # Sell if coin is at or above maximum price boundary
            print("Price above target. Selling.") 
        else:
            print("No trades desireable at this time. Checking back later.")
        i += 1
        if __debug__ and i >= 4:
            print("Completed debug run. Breaking.")
            break
        time.sleep(6)
        