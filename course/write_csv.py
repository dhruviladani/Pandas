import pandas as pd

dic = {"a": [1,2,3,4,5,6] , "s":[1,2,3,4,5,6], "d": [1,2,3,4,5,6]}

d = pd.DataFrame(dic)

d

d.to_csv("Test_new.csv", index=False)

df = pd.read_csv("Test_new.csv",nrows=2)
df

df1 = pd.read_csv("Test_new.csv",index_col='a')
df1

df2 = pd.read_csv("Test_new.csv",names=["c1","c2","c3"])
df2