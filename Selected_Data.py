import pandas as pd

def selectData(students):
    df=students.loc[students['student_id']==101,['name','age']]
    return df
    