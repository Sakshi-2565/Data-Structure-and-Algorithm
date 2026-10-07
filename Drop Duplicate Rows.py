import pandas as pd

def dropDuplicateEmails(customers):
    df=customers.drop_duplicates(subset=['email'])
    return df
    