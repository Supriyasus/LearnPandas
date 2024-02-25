import pandas as pd
var=pd.DataFrame({"Days":[1,2,3,4,5,6],"Eng":[11,22,33,44,55,66],"Math":[66,55,44,33,22,11]})
print(pd.melt(var))
print(pd.melt(var,id_vars="Days"))
print(pd.melt(var,id_vars="Days",var_name="Subject",value_name="Marks"))
print()

var2=pd.DataFrame({"Days":[1,2,3,4,5,6],"Name":["a","b","c","a","b","c"],"Eng":[11,22,33,44,55,66],"Math":[66,55,44,33,22,11]})
print(var2.pivot(index="Days",columns="Name"))
print(var2.pivot(index="Days",columns="Name",values="Eng"))