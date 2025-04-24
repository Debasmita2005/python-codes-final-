#This progaram write a menu-driven program to implement the stack data structure
stack = []

def is_empty():
    return len(stack) == 0

def push():
    item = input("Enter the item to push onto the stack: ")
    stack.append(item)  
    print(f"{item} has been pushed onto the stack")

def pop():
    if is_empty():
        print("Stack is empty")
    else:
        print(f"Popped item: {stack.pop()}")  

def peek():
    if is_empty():
        print("Stack is empty")
    else:
        print(f"Top item: {stack[-1]}")

def display():
    if is_empty():
        print("Stack is empty")
    else:
        print(f"Stack elements (from top to bottom): {stack[::-1]}")

def stack_menu():
    while True:
        print("\nStack menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")
        c = input("Enter your choice (1-5): ")
        if c == "1":
            push()
        elif c == "2":
            pop()
        elif c == "3":
            peek()
        elif c == "4":
            display()
        elif c == "5":
            print("End of the program")
            break
        else:
            print("Please enter choice between 1 to 5")

stack_menu()
