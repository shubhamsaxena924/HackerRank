
def palin(num):
    rev,r=0,0
    n=num
    while(num>0):
        r=num%10
        num=num//10
        rev=(10*rev)+r
    if rev==n:
        return True
    else:
        return False
n,m=int(input()),list(map(int,input().split()))
ans=True
ansj=False
for i in m:
    if(i<0):
        ans=False
for i in m:
    if(palin(i)==True):
        ansj=True
print(ans and ansj)
