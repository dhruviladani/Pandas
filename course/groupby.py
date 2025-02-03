import pandas as pd

var = pd.DataFrame({"name": ["a",'b','c','d',"a",'b','c','d'], "s1": [1,2,3,4,5,6,7,8],"s2": [8,7,6,5,4,3,2,1]})
var

v = var.groupby('name')
v

print(v)

v = var.groupby('name')
v

for x,y in v:
    print(x)
    print(y)
    print()