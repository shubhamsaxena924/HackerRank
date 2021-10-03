K=int(input())
L=[int(i) for i in input().split()]
S=set(L)
print((sum(S)*K-sum(L))//(K-1))