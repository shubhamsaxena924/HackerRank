l=list(map(int,input().split()))
N,X=l[0],l[1]
m=[]
for i in range(X):
    m.append(list(map(float,input().split())))
n=zip(*m)
for i in n:
    sum=0
    for j in range(X):
        sum=sum+i[j]
    print(float(sum/X))

