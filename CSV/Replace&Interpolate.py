import pandas as pd

x=pd.read_csv(r"C:\\Users\\supriya shrivastv\\PycharmProjects\\Pandas\\Dataset\\1000_popular_hindi_spotify")
print(x)
var1=x.replace(to_replace="Hindia",value="Hindi")
print(var1)
