import pandas as pd

def fillMissingValues(products):
    product=products.fillna({'quantity': 0})
    return product