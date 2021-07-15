import pandas as pd
import numpy as np

thedata=pd.read_csv('samplefile3.csv')
themeans=list(thedata.mean())
print(themeans)

nas=list(thedata.isna().sum())
print(nas)

thedata['col1'].fillna(pd.to_numeric(thedata['col1'],errors='coerce').mean(skipna=True), inplace = True)

thedata['col2'].fillna(pd.to_numeric(thedata['col2'],errors='coerce').mean(skipna=True), inplace = True)
thedata['col3'].fillna(pd.to_numeric(thedata['col3'],errors='coerce').mean(skipna=True), inplace = True)

