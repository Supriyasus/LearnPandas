import pandas as pd
x=pd.read_csv("C:\\Users\\supriya shrivastv\\PycharmProjects\\Pandas\\archive\\1000_popular_hindi_spotify.csv")
print(x)
var=x.index#top and bottom index of file
print(var)
var2=x.columns#Name of all the headers of columns
print(var2)
var3=x.describe()#Give mean,count etc value of numerical entries
print(var3)
var4=x.head()
print(var4)
var5=x.head(8)
print(var5)
var6=x.tail()
print(var6)
print(x[6:10])
print(x.index.array)
print(x.sort_index(axis=0,ascending=False))
var7=x.loc[3,"Popularity"]=8
print(x)
var8=x.loc[[3,4,5],["ID","Artists"]]
print(var8)
var9=x.iloc[0,1]
print(var9)
var10=x.drop("ID",axis=1)
print(var10)