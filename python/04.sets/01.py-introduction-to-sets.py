def average(array):
    array = set(array)
    sum = 0
    for i in array:
        sum = sum+i
    return sum/len(array)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
