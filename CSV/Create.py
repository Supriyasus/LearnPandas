import pandas as pd
x={"a":(1,2,3),"b":(4,5,6),"c":(2,5,3),1:(9,0,8)}
val=pd.DataFrame(x)
val.to_csv("Test2.csv",index=False,header=["A","B","C","D"])