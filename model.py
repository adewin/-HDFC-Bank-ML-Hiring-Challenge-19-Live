import numpy as np
import pandas as pd

df=pd.read_csv("Train.csv")

df=df[1:10]
p=df['Col3']
df.isnull().any(axis=0)
df1=pd.DataFrame()
for i in range(3,999):
    Check_Nan=(df['Col{}'.format(i)].isnull().any(axis=0))
    #if Nan value found then if condition true
    if  Check_Nan:
        print("****************before****************")
        print(df['Col{}'.format(i)])
        df['Col{}'.format(i)]=df['Col{}'.format(i)].fillna(np.mean(df['Col{}'.format(i)]))
        print("************after*********************")
        print(df['Col{}'.format(i)])
        
        
for i in range(3,len(df)):
    p=all(df['Col138'].isnull())
    if p :
        df1['Col{}'.format(i)]=df.drop(['Col{}'.format(i)],axis=1)




df['Col13'].isnull()   

p=all(df['Col138'].isnull())
p

#first remove those columns that contains only 
df=df.drop(['Col1'],axis=1)