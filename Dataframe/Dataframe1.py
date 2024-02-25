import pandas as pd
#y=(1,2,3,4,5,6)
x={"a":(1,2,3),"b":(4,5,6),"c":(2,5,3),1:(9,0,8)}
val=pd.DataFrame(x,columns=["a",1])
#val2=pd.DataFrame(y)
#print(val2)
#print(val)
#print(type(val))
print(val["a"][2])