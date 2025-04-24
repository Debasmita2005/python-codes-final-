#This program calculate net sales
def net_sales():
    gs = float(input("Enter the gross sales:"))
    ns = 0.9 * gs
    print("Net sales:", ns)

net_sales()
