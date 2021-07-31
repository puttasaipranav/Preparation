import pandas as pd
import matplotlib.pyplot as ply

df = pd.read_csv("age.csv",header=2)
n=1
df.drop(df.tail(n).index, inplace = True)

f=df["Age"]=="18 - 24"
g=df.loc[f]
conv=g["Impr."]
conv = conv.str.replace(',','').astype(int)
con=conv.sum()
cos=g["Clicks"]
cos = cos.str.replace(',','').astype(int)
cos= cos.sum()
ctr = cos/con*100

a=df["Age"]=="25 - 34"
b=df.loc[a]
mconv=b["Impr."]
mconv = mconv.str.replace(',','').astype(int)
mcon=mconv.sum()
mcos=b["Clicks"]
mcos = mcos.str.replace(',','').astype(int)
mcos= mcos.sum()
mctr = mcos/mcon*100

c=df["Age"]=="35 - 44"
d=df.loc[c]
tconv=d["Impr."]
tconv = tconv.str.replace(',','').astype(int)
tcon=tconv.sum()
tcos=d["Clicks"]
tcos = tcos.str.replace(',','').astype(int)
tcos= tcos.sum()
tctr = tcos/tcon*100

h=df["Age"]=="45 - 54"
i=df.loc[h]
wconv=i["Impr."]
wconv = wconv.str.replace(',','').astype(int)
wcon=wconv.sum()
wcos=i["Clicks"]
wcos = wcos.str.replace(',','').astype(int)
wcos= wcos.sum()
wctr = wcos/wcon*100

j=df["Age"]=="55 - 64"
k=df.loc[j]
thconv=k["Impr."]
thconv = thconv.str.replace(',','').astype(int)
thcon=thconv.sum()
thcos=k["Clicks"]
thcos = thcos.str.replace(',','').astype(int)
thcos= thcos.sum()
thctr = thcos/thcon*100

l=df["Age"]=="65+"
m=df.loc[l]
fconv=m["Impr."]
fconv = fconv.str.replace(',','').astype(int)
fcon=fconv.sum()
fcos=m["Clicks"]
fcos = fcos.str.replace(',','').astype(int)
fcos= fcos.sum()
fctr = fcos/fcon*100

n=df["Age"]=="Unknown"
o=df.loc[n]
sconv=o["Impr."]
sconv = sconv.str.replace(',','').astype(int)
scon=sconv.sum()
scos=o["Clicks"]
scos = scos.str.replace(',','').astype(int)
scos= scos.sum()
sctr = scos/scon*100

print('Clicks')
print('Sunday Clicks :',cos)
print('Monday Clicks :',mcos)
print('Tuesday Clicks :',tcos)
print('Wednesday Clicks :',wcos)
print('Thrusday Clicks :',thcos)
print('Friday Clicks :',fcos) 
print('Saturday Clicks :',scos)

print('CTR')
print('Sunday Ctr :',ctr)
print('Monday Ctr :',mctr)
print('Tuesday Ctr :',tctr)
print('Wednesday Ctr :',wctr)
print('Thrusday Ctr :',thctr)
print('Friday Ctr :',fctr)
print('Saturday Ctr :',sctr)

lis=[]
lis.append(ctr)
lis.append(mctr)
lis.append(tctr)
lis.append(wctr)
lis.append(thctr)
lis.append(fctr)
lis.append(sctr)


plt.plot(lis,marker='o')