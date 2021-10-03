import os


def solve(s):
    l = s.split()
    for x in l:
        s = s.replace(x, x.capitalize())
    return s


# This will not work on local
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
