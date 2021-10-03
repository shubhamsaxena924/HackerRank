l=[]
for _ in range(int(input())):
    com=input().split()
    if(com[0]=="print"):
        print(l)
    elif(com[0]=="append"):
        l.append(int(com[1]))
    elif(com[0]=="sort"):
        l=sorted(l)
    elif(com[0]=="pop"):
        l.pop()
    elif(com[0]=="reverse"):
        l.reverse()
    elif(com[0]=="remove"):
        l.remove(int(com[1]))
    elif(com[0]=="insert"):
        l.insert(int(com[1]),int(com[2]))