import pandas as pd

var = pd.DataFrame({"days": [1,2,3,4,5,6], "eng": [10,11,12,13,14,15], "maths": [16,17,18,19,20,21]})

var

pd.melt(var,id_vars=["days"], var_name="subjects")


var = pd.DataFrame({"days": [1,2,3,4,5,6], 
                    "st_name":['a','b','c','a','b','c'], "eng": [10,11,12,13,14,15], "maths": [16,17,18,19,20,21]})

var

var.pivot(index="days",  columns="st_name", values="eng")

var = pd.DataFrame({"days": [1,1,1,1,2,2], 
                    "st_name":['a','b','c','a','b','c'], "eng": [10,11,12,13,14,15], "maths": [16,17,18,19,20,21]})

var.pivot_table(index="st_name", columns="days", aggfunc="sum")