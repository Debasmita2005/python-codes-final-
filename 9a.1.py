# Define three functions
def fun():
    print("This is fun() function")

def disp():
    print("This is disp() function")

def msg():
    print("This is msg() function")

# Store functions in a list
function_list = [fun, disp, msg]

# Call each function in the list using a loop
print("Calling functions from list:")
for i, func in enumerate(function_list):
    print(f"Calling function {i+1}:", end=" ")
    func()  # Call the function

print("\nAnother way to iterate:")
for func in function_list:
    func()  # Call the function
