#This progaram write a menu-driven program to implement the queue data structure
queue = []

def is_empty():
    return len(queue) == 0

def enqueue():
    item = input("Enter the item to enqueue: ")
    queue.append(item)  
    print(f"{item} has been added to the queue")

def dequeue():
    if is_empty():
        print("Queue is empty")
    else:
        print(f"Dequeued item: {queue.pop(0)}") 

def peek():
    if is_empty():
        print("Queue is empty")
    else:
        print(f"Front item: {queue[0]}")  

def display():
    if is_empty():
        print("Queue is empty")
    else:
        print(f"Queue elements (from front to rear): {queue}")

def queue_menu():
    while True:
        print("\nQueue menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Exit")
        c = input("Enter your choice (1-5): ")
        if c == "1":
            enqueue()
        elif c == "2":
            dequeue()
        elif c == "3":
            peek()
        elif c == "4":
            display()
        elif c == "5":
            print("End of the program")
            break
        else:
            print("Please enter choice between 1 to 5")

queue_menu()
