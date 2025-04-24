#This program calculate Permutation and Combination
n = int(input("Enter total number of items:"))
r = int(input("Enter number of item chosen:"))

def nPr_nCr():
    if n >= r:
        s = n - r
        N, D, R = 1, 1, 1
        for i in range(2, n + 1):
            N *= i
        for i in range(2, s + 1):
            D *= i
        for i in range(2, r + 1):
            R *= i
        print(f"Permutation:{int(N / D)}")
        print(f"Combination:{int(N / (R * D))}")
    else:
        print("Invalid input")

nPr_nCr()
