import pandas as pd
var={"A":(1,2,3,4),"B":(5,6,7,8),1:(7,8,9,0)}
x=pd.DataFrame(var)
x.insert(1,"Python",var[1])
print(x)
x["New"]=x["A"][:2]
print(x)
#Delete
var2=x.pop("Python")
print(var2)
print(x)