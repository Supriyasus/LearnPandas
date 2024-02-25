
import pandas as pd
x=[1,2,3,4,5]
new=pd.Series(x)
print(new)
print(type(new))
changeindex=pd.Series(x,index=('a','b','c','d','e'),dtype=float,name="Series")
print(changeindex)