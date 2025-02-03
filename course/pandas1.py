import pandas as pd

x = [1,2,3]

var = pd.Series(x,index=['a','b','c'],dtype="float", name="python")

print(var)
print(type(var))


dic = {"name" : ['python','c','c++','java'],"p": [12,13,14,15], "rank" : [1,4,6,8]}

v1 = pd.Series(dic)
v1


s = pd.Series(12, index=[1,2,3,4,5])

print(s) 

s1 = pd.Series(12, index=[1,2,3,4,5])
s2 = pd.Series(12, index=[1,2,3])

print(s1 + s2)


##############

l = [1,2,3,4,5]

var =  pd.DataFrame(l)
print(type(var))


d = {"a":[1,2,3,4,5], "b":[1,2,3,4,5]}

var1 = pd.DataFrame(d)
var2 = pd.DataFrame(d,columns=["a"])

print(var1)
print(var2)
print(var1["a"][3])

l1 = [[1,2,3,4,5],[3,4,5,6,7]]
var3 = pd.DataFrame(l1)

print(var3)

sr = {"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,3])}

var4 = pd.DataFrame(sr)

print(var4)


#############

v = pd.DataFrame({"a":[1,2,3,4,5], "b":[1,2,3,4,5]})

v['c'] = v['a'] + v['b']

v

v['c'] = v['a'] - v['b']
v

v['python'] = v['a'] <= 4
v

##############
#Insert

var = pd.DataFrame({"A":[1,2,3,4,5], "B":[3,4,5,6,7], "C":[11,22,33,44,55]})

var

var.insert(1, 'python_1', [5,6,7,8,9])

var

var["python"] = var["A"][:3]

var

var1 = var.pop("B")
var1

del var["A"]
var

