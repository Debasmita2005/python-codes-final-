def compute(n):
    # Convert n to string for easier manipulation
    n_str = str(n)
    
    # Calculate nn, nnn, nnnn
    nn = int(n_str + n_str)
    nnn = int(n_str + n_str + n_str)
    nnnn = int(n_str + n_str + n_str + n_str)
    
    # Calculate sum
    total = n + nn + nnn + nnnn
    
    return total

# Test the function for digits 4 to 7
for digit in range(4, 8):
    result = compute(digit)
    print(f"For n = {digit}, n + nn + nnn + nnnn = {digit} + {digit}{digit} + {digit}{digit}{digit} + {digit}{digit}{digit}{digit} = {result}")
