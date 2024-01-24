divder = ("=" * 6)

replay = "y"
while replay == "y":
    num = int(input("Enter an integer: "))
    print("{:<10} {:<10} {:<10}".format("Number", "Squared", "Cubed"))
    print("{:<10} {:<10} {:<10}".format(divder, divder, divder))
    for i in range(num):
        print("{:<10} {:<10} {:<10}".format(i +1, i**2 +1, i**3 +1))
    print("----------")
    for x in range(1, num+1):
        for y in range(1, num+1):
            print(f'{x*y}', end=" ")
        print()
    replay = input("Continue? (y/n): ")
