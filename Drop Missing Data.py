import pandas as pd

def dropMissingData(student):
    df=student.dropna(subset=['name'], inplace=False)
    return df