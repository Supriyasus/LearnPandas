import pandas as pd
x={"name":('X','Y'),"number":(1,2)}
ser=pd.Series(x)
print(ser)
print(type(ser))