import pandas as pd

def concatenateTables(df1,df2):
    df=pd.concat([df1,df2],axis=0)
    return df