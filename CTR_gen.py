import pandas as pd
import matplotlib.pyplot as ply

df = pd.read_csv("gen.csv",header=2)
n=1
df.drop(df.tail(n).index, inplace = True)

f=df["Gender"]=="Male"
g=df.loc[f]
conv=g["Impr."]
conv = conv.str.replace(',','').astype(int)
con=conv.sum()
cos=g["Clicks"]
cos = cos.str.replace(',','').astype(int)
cos= cos.sum()
ctr = cos/con*100

a= df['Gender']=='Female'
b= df.loc[a]
mconv= b['Impr.'].str.replace(',','').astype(int)
mconv=mconv.sum()
mcos=b['Clicks'].str.replace(',','').astype(int)
mcos=mcos.sum()
mctr=mcos/mconv*100

c= df['Gender']=='Unknown'
d= df.loc[c]
nconv= d['Impr.'].str.replace(',','').astype(int)
nconv= nconv.sum()
ncos= d['Clicks'].str.replace(',','').astype(int)
ncos= ncos.sum()
nctr= ncos/nconv*100

print("Clicks")
print("Male Clicks:",cos)
print("Female Clicks:",mcos)
print("Unknown Clicks:",ncos)

print("CTR's")
print("Male CTR: $",ctr)
print("Female CTR: $",mctr)
print("Unknown CTR: $",nctr)

lis=[]
lis.append(ctr)
lis.append(mctr)
lis.append(nctr)

mylables=['Male','Female','Unknown']
plt.plot(lis,marker='o')