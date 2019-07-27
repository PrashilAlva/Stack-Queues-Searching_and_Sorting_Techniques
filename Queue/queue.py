class Stack:

    def __init__(self):
        self.st=[]

    def push(self):
        num=int(input("Enter the element to push"))
        self.st.append(num)
        print("Element Pushed")

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            ele=self.st.pop()
            print(f"Element Popped is {ele}")

    def display(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print("Elements in the Stack are:")
            for i in range(len(self.st)-1,-1,-1):
                print(self.st[i])

    
    def show(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            num=int(input('Enter the element to search?'))
            if num in self.st:
                print(f"Element found at position {self.st.index(num)+1}")
            else:
                print("Element not found!")
        

    def is_empty(self):
        if len(self.st) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    st=Stack()
    while True:
        print('*'*100)
        print('1.PUSH 2.POP 3.DISPLAY 4.SEARCH 5.EXIT')
        print('*'*100)
        try:
            ch=int(input('Enter your choice?'))
        except (KeyError,ValueError):
            print("Invalid Input!Try again...")