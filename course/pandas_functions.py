import pandas as pd

df = pd.read_csv("Test_new.csv")
df


df.index

df.columns

df.describe()

df.head(2)

df.tail(2)

df[:1]

df[:2]

df.index.array

import numpy as np

v = np.asarray(df)
v


df.sort_index(axis=0, ascending=False)

df["a"][0] = "python"
df

df.loc[0,"a"]= "py"
df

df.loc[[2,3,4],["a","s"]]

df.iloc[0]

df.iloc[3,1]

