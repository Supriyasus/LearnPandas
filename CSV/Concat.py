import pandas as pd
var1=pd.DataFrame({"ID":[1,2,3,4,5,6,7,8,9,10],"Name":["A","B","C","D","E","F","G","H","I","J"]})
var2=pd.DataFrame({"ID":[1,2,3,4,5,6,7,8,9,10],"Number":["11","22","33","44","55","66","77","88","99","00"]})
print(pd.concat([var1,var2]))
print(pd.concat([var1,var2],join="inner"))
print(pd.concat([var1,var2],join="outer"))
print(pd.concat([var1,var2],join="inner",keys=["var1","var2"]))
print(pd.concat([var1,var2],axis=1,join="inner",keys=["var1","var2"]))