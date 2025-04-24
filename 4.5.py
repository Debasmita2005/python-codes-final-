#This program generate all Pythgorean triplets with side length <= 30

def pythagorean_triplets():
    print("Pythagorean Triplets with side length <= 30:")
    for i in range(1, 31):
        for j in range(i, 31):
            for k in range(j, 31):
                if i ** 2 + j ** 2 == k ** 2 and i < k and j < k:
                    print(f"({i}, {j}, {k})")

pythagorean_triplets()
