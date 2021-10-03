def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        l = []
        s = string[i:i+k]
        for j in s:
            if(j not in l):
                l.append(j)
        print(''.join(l))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
