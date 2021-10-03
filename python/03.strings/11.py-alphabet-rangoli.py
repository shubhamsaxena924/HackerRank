def print_rangoli(size):
    for i in range(size-1, -1, -1):
        print(2*i*'-', end='')
        for j in range(1, size-i+1):
            print(chr(size-j+97), end='')
            if(i != size-1):
                print('-', end='')
        for j in range(size-i-2, -1, -1):
            print(chr(size-j+96), end='')
            if(j > 0):
                print('-', end='')
        print(2*i*'-', end='')
        print()
    for i in range(1, size):
        print(2*i*'-', end='')
        for j in range(1, size-i+1):
            print(chr(size-j+97), end='')
            if(i != size-1):
                print('-', end='')
        for j in range(size-i-2, -1, -1):
            print(chr(size-j+96), end='')
            if(j > 0):
                print('-', end='')
        print(2*i*'-', end='')
        print()


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
