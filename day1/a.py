import pandas as pd



data=["sam","tom","arun"]
data_series=pd.Series(data,index=["a","b","c"])
print (data_series)
print(type(data_series))