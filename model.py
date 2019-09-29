import numpy as np
import pandas as pd

df=pd.read_csv("Train.csv")

df=df[1:10]

#remove those columns that have 70% null values 
for i in range(3,999):
    try:
        sum_Nan=df['Col{}'.format(i)].isnull().sum()
        #70% data nan then remove columns
        #
        x70=(17521*7)/10
        x50=(17521*5)/10
        #if Nan value found then if condition true
        if sum_Nan >=x70:
            df=df.drop(['Col{}'.format(i)],axis=1)
           #if columns have morethan 50% data nan value and less 70% then  direct fill with 0 
        elif  sum_Nan <x70 and sum_Nan>x50:
            df['Col{}'.format(i)]=df['Col{}'.format(i)].fillna(np.mean(0))

        elif sum_Nan<x50:
            #then fill mean values
            df['Col{}'.format(i)]=df['Col{}'.format(i)].fillna(np.mean(df['Col{}'.format(i)]))


    except KeyError:
        pass


        
        
for i in range(3,2395):
    try:
        p=all(df['Col{}'.format(i)].isnull())
        if p :
            df=df.drop(['Col{}'.format(i)],axis=1)
    except KeyError:
        pass


df['Col37'].isnull().sum()