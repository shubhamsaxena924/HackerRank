n=int(input())
l=[]
for i in range(n):      
    l.append(input().split())
m=input()
for i in range(n):
    if(m==l[i][0]):
        a=(float(l[i][1])+float(l[i][2])+float(l[i][3]))/3
        print('%.2f'%a)
        break