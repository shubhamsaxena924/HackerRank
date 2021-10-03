N=set(input().split())
a=int(input())
for i in range(a):
    command=input().split()
    M=set(input().split())
    if command[0]=='update':
        N.update(M)
    elif command[0]=='intersection_update':
        N.intersection_update(M)
    elif command[0]=='difference_update':
        N.difference_update(M)
    elif command[0]=='symmetric_difference_update':
        N.symmetric_difference_update(M)
print(sum([int(i) for i in N]))

