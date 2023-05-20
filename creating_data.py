import pandas as pd # to read the data set 
from random import randint
data = pd.read_csv('./archive/flights.csv')
col1 = data.loc[: , 'from']
col2 = data.loc[: , 'to']
merged = list(set(col1) | set(col2))
attractions = [randint(1, 5) for _ in range(9)]
prices = [randint(277, 3000) for _ in range(9)]
mydf = pd.DataFrame() 
mydf['cities'] = merged
mydf['attractions'] = attractions
mydf['prices'] = prices
print(mydf)
mydf.to_csv('final_data.csv' , index= False)