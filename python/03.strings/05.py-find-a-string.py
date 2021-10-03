def count_substring(string, sub_string):
    count=0
    c=0
    for i in range(0,len(string)):
        if(string.find(sub_string,c,len(string)+1)!=-1):
            d=string.find(sub_string,c,len(string)+1)
            count=count+1
            c=d+1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

