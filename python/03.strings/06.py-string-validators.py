s = input()
a,b,c,d,e=False,False,False,False,False
for i in s:
    if(i.isalnum()==True):
        a=True
    if(i.isalpha()==True):
        b=True
    if(i.isdigit()==True):
        c=True
    if(i.islower()==True):
        d=True
    if(i.isupper()==True):
        e=True
print(a,b,c,d,e,sep="\n")