import pandas as pd
var1=pd.DataFrame({"ID":[1,2,3,4,5,6,7,8,9,10],"Name":["A","B","C","D","E","F","G","H","I","J"]})
var2=pd.DataFrame({"ID":[1,2,3,4,5,6,7,8,9,10],"Number":["11","22","33","44","55","66","77","88","99","00"]})
print(pd.merge(var1,var2,on="ID"))

var1=pd.DataFrame({"ID":[1,2,3,4,5,6,7,8,9,10],"Name":["A","B","C","D","E","F","G","H","I","J"]})
var2=pd.DataFrame({"ID":[1,2,3,4,5,11,22,33,44,55],"Number":["11","22","33","44","55","66","77","88","99","00"]})
print(pd.merge(var1,var2,on="ID"))
print(pd.merge(var1,var2,how="left"))
print(pd.merge(var1,var2,how="right"))
print(pd.merge(var1,var2,how="outer"))
print(pd.merge(var1,var2,how="outer",indicator=True))

var1=pd.DataFrame({"ID":[1,2,3,4,5,6,7,8,9,10],"Name":["A","B","C","D","E","F","G","H","I","J"]})
var2=pd.DataFrame({"ID":[1,2,3,4,5,11,22,33,44,55],"Name":["11","22","33","44","55","66","77","88","99","00"]})
print(pd.merge(var1,var2,left_index=True,right_index=True))
print(pd.merge(var1,var2,left_index=True,right_index=True,suffixes=("_Emp","_Cust")))