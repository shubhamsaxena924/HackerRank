A = set(input().split())
n = int(input())
flag = None
for _ in range(n):
    B = set(input().split())
    flag = A.issuperset(B) and len(A) > len(B)
    if(flag == False):
        break
print(flag)
