import math
a = complex(input())
print((a.real**2+a.imag**2)**(1/2))
if(a.real > 0):
    print(math.atan(a.imag/a.real))
elif(a.real < 0 and a.imag < 0):
    print(math.atan(a.imag/a.real)-3.141)
elif(a.real < 0 and a.imag > 0):
    print(math.atan(a.imag/a.real)+3.141)
elif(a.real == 0 and a.imag > 0):
    print(math.atan(-(math.inf))+3.141)
elif(a.real == 0 and a.imag < 0):
    print(math.atan(math.inf)-3.141)
