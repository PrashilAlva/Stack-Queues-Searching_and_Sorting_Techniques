def binnsearch(lst,l,h,key):
    if l <= h:
        mid=(l+h)//2
        if lst[mid]==key:
            return True
        elif lst[mid]<key:
            binnsearch(lst,mid+1,h,key)
        else:
            binnsearch(lst,l,mid-1,key)
    return False

if __name__ == "__main__":
    lst=[]
    while True:
        num=input('Enter the element to insert to list or press q to exit')
        if num=='q':
            break
        lst.append(int(num))
    
    key=int(input('Enter the element to search'))
    index=binnsearch(lst,0,len(lst)-1,key)
    if index:
        print(f"{key} is found!")
    else:
        print(f'{key} not found')