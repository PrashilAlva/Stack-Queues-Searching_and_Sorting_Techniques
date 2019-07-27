def bubblesort(lst):

    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]

l=[7,2,9,3,1,0]
print(l)
bubblesort(l)
print(l)