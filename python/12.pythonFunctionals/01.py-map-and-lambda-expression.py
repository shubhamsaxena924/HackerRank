cube = lambda x:x*x*x # complete the lambda function 

def fibonacci(n):
    l=[]
    a,b=0,1
    if(n>0):
        l.append(a)
        if(n>1):
            l.append(b)
    for i in range(n-2):
        sum=a+b
        l.append(sum)
        a=b
        b=sum
    return l    
# return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

