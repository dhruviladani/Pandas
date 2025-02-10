import pandas as pd
import numpy as np


df = pd.read_csv("files/braintree_.csv")

# df.insert(column= "Country", )

country = ['US','IntI']
df["Country"] = np.random.choice(country, size=len(df))

df

data = df[df['Month'] == 1]

pivot = df.pivot_table(
    data,
    
    index= ["Country", "Response"],
    columns= ['Year', 'Month'],
    aggfunc= {'Response': ['count'].count()}
)

pivot

# sum = df.loc[pd.Index(["Response"])]

pivot1 = df.pivot_table(
    data,
    
    index= ["Country", "Response"],
    columns= ['Year', 'Month']
    
)

pivot1