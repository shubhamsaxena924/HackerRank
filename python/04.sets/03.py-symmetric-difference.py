m=int(input())
a=set(input().split())
n=int(input())
b=set(input().split())
l=sorted(list(map(int,a.union(b)-a.intersection(b))))
for i in l:
    print(i)