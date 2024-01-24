divder = ("=" * 6)

replay = "y"
while replay == "y":
    num = int(input("Enter an integer: "))
    print("{:<10} {:<10} {:<10}".format("Number", "Squared", "Cubed"))
    print("{:<10} {:<10} {:<10}".format(divder, divder, divder))
    for i in range(num):
        print("{:<10} {:<10} {:<10}".format(i+1, (i+1)**2, (i+1)**3))

    for i in range(1, num + 1):
        print(f"\t{i:3d}", end="")
    print()

    for i in range(1, num + 1):
        print(f'\t''  =', end="")
    print()

    for i in range(1, num + 1):
        print(f"{i} |", end="")
        for j in range(1, num + 1):
            result = i * j
            print(f" {result:3d}", end="")
        print()
    replay = input("Continue? (y/n): ")
