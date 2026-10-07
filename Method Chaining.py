import pandas as pd

def findHeavyAnimals(animals):
    return (
        animals.query("weight > 100").sort_values(by="weight", ascending=False)[["name"]]                  
    )