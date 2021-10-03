if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list=[]
    for x in arr:
        if x not in list:
            list.append(x)
    list.sort()
    print(list[-2])
