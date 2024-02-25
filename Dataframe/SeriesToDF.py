import pandas as pd
x={"a":pd.Series([1,2,3]),"b":pd.Series([4,5,6])}
val=pd.DataFrame(x)
print(val)