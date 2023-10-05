from api import *
from classes import Asset

def Bangbang(asset):
    bidask = currentAssetPrice(asset.assetName)
    # Sell if coin is at or above maximum price boundary
    # Buy if coin is below minimum price boundary.
    pass