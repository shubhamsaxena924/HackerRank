n=int(input())
l=[]
for i in range(n):
    m=[]
    m.append(input())
    m.append(float(input()))
    l.append(m)
k=[]
for i in range(n):
    k.append(l[i][1])
j=sorted(k)
c=j.count(j[0])
min=j[c]
o=[]
for i in range(n):
    if(l[i][1]==min):
        o.append(l[i][0])
o=sorted(o)
for i in o:
    print(i)