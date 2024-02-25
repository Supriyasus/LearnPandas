import pandas as pd
var={"A":(1,2,3,4),"B":(5,6,7,8),1:(7,8,9,0)}
x=pd.DataFrame(var)
x["Pyth"]=x["A"]<=3
print(x)