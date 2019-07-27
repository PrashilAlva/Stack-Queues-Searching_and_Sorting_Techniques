def binsearch(lst,ele):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==ele:
            return True
        elif lst[mid]>ele:
            high=mid-1
        else:
            low=mid+1

    return False

if __name__ == "__main__":
    lst=[]
    while True:
        num=input('Enter the element to insert to list or press q to exit')
        if num=='q':
            break
        lst.append(int(num))
    
    key=int(input('Enter the element to search'))
    index=binsearch(lst,key)
    if index:
        print(f"{key} is found!")
    else:
        print(f'{key} not found')