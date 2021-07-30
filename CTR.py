import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("d.csv",header=2)
n=1
df.drop(df.tail(n).index, inplace = True)

f=df["Device"]=="Computers"
g=df.loc[f]
conv=g["Impr."]
conv = conv.str.replace(',','').astype(int)
con=conv.sum()
cos=g["Clicks"]
cos = cos.str.replace(',','').astype(int)
cos= cos.sum()
ctr = cos/con*100

a= df['Device']=='Mobile phones'
b= df.loc[a]
mconv= b['Impr.'].str.replace(',','').astype(int)
mconv=mconv.sum()
mcos=b['Clicks'].str.replace(',','').astype(int)
mcos=mcos.sum()
mctr=mcos/mconv*100

c= df['Device']=='Tablets'
d= df.loc[c]
nconv= d['Impr.'].str.replace(',','').astype(int)
nconv= nconv.sum()
ncos= d['Clicks'].str.replace(',','').astype(int)
ncos= ncos.sum()
nctr= ncos/nconv*100

print("Clicks")
print("C Clicks:",cos)
print("M Clicks:",mcos)
print("T Clicks:",ncos)

print("CTR's")
print("C CTR: $",ctr)
print("M CTR: $",mctr)
print("T CTR: $",nctr)

lis=[]
lis.append(ctr)
lis.append(mctr)
lis.append(nctr)


mylabels=['computers','Mobile','Tablet']
plt.pie(lis,labels=mylabels)