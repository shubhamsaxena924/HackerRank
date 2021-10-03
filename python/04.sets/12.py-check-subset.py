for _ in range(int(input())):
    n = input()
    N = set(input().split())
    b = input()
    B = set(input().split())
    print(N.issubset(B))
