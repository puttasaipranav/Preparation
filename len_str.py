def leng(a):
    g=[]
    for i in a:
        if len(i)>=2:
            g.append(i)
    print(len(g))
leng(['sai','f','fg'])