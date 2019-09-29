import numpy as np
import pandas as pd

df=pd.read_csv("Train.csv")

df=df[1:10]
p=df['Col3']
df.isnull().any(axis=0)

for i in range(3,999):
    Check_Nan=(df['Col{}'.format(i)].isnull().any(axis=0))
    #if Nan value found then if condition true
    if  Check_Nan:
        print("****************before****************")
        print(df['Col{}'.format(i)])
        df['Col{}'.format(i)]=df['Col{}'.format(i)].fillna(np.mean(df['Col{}'.format(i)]))
        print("************after*********************")
        print(df['Col{}'.format(i)])
        
        
        
df['Col139'].notnull().any(axis=0)    