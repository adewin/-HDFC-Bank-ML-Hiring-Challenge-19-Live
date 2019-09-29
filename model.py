import numpy as np
import pandas as pd

df=pd.read_csv("Train.csv")

df=df[1:10]
p=df['Col3']
df.isnull().any(axis=0)

for i in range(3,20):
    print(df['Col{}'.format(i)].isnull().any(axis=0))