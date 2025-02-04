import pandas as pd

var1 = pd.DataFrame({"A": [1,2,3,4,5], "B": [6,7,8,9,0]}, index=['a','b','c','d','e'])
var2 = pd.DataFrame({"C": [11,22], "D":[66,77]}, index=['a','b'])

var1.join(var2)
var2.join(var1)

var2.join(var1, how= "right")
var2.join(var1, how= "outer")
var2.join(var1, how= "inner")

var1 = pd.DataFrame({"A": [1,2,3,4,5], "B": [6,7,8,9,0]})
var2 = pd.DataFrame({"C": [11,22], "B":[66,77]})

var2.join(var1, how= "outer", lsuffix="_1")


#append

var1.append(var2)