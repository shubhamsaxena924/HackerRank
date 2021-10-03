def print_formatted(number):
    s = len('{:b}'.format(number))
    for i in range(1, number+1):
        print('{:{s}d} {:{s}o} {:{s}X} {:{s}b}'.format(i, i, i, i, s=s))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
