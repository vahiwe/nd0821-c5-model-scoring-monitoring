import ast
import pandas as pd

with open('healthdata.txt', 'r') as f:
    meanslist = ast.literal_eval(f.read())

thedata=pd.read_csv('bloodpressure.csv')
themeans=list(thedata.mean())

meancomparison=[(themeans[i]-meanslist[i])/meanslist[i] for i in range(len(meanslist))]
print(meancomparison)

nas=list(thedata.isna().sum())
print(nas)