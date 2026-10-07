import pandas as pd

def pivotTable(weather):
    df=weather.pivot(index='month', columns='city',values='temperature')
    return df
