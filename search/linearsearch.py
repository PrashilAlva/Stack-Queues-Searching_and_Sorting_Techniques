def searchLinear(lst,ele):
    count=0
    for i in lst:
        if ele==i:
            return count
        count=count+1

if __name__ == "__main__":
    lst=[]
    while True:
        num=input('Enter the element to insert to list or press q to exit')
        if num=='q':
            break
        lst.append(int(num))
    
    key=int(input('Enter the element to search'))
    index=searchLinear(lst,key)
    print(index+1)