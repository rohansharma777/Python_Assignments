x = int(input("Enter the you want to check if it's a prime"))
i = 2
while i < x:
    d = x % i
    if d == 0:
        print("It's not a prime no.")
        break
    i += 1
if x == i:
    print("It's a prime no.")
