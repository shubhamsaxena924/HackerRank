l = input().split()
a = int(l[0])
b = int(l[1])
for i in range(a//2):
    dash = ((b-(3*(2*i+1)))//2)*'-'
    print(dash, '.|.'*(2*i+1), dash, sep='')
print(((b-7)//2)*'-', 'WELCOME', ((b-7)//2)*'-', sep='')
for i in range(a//2-1, -1, -1):
    dash = ((b-(3*(2*i+1)))//2)*'-'
    print(dash, '.|.'*(2*i+1), dash, sep='')
