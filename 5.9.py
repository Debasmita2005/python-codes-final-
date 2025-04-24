#This program prints a list of those numbers from first list which are not in second list
lst1 = list(map(int, input("Enter first list separated by space:").split()))
lst2 = list(map(int, input("Enter second list separated by space:").split()))

def separate_lst():
    lst3 = [x for x in lst1 if x not in lst2]
    print(f"Third list of unique numbers:{lst3}")
    
separate_lst()
