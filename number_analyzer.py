user_name = input("What's your name?: ")
playing = "y"

while playing == "y":
    integer = int(input(f"{user_name} give me a number between 1 and 100: "))
    while integer <= 0 or integer > 100:
        integer = int(input(f"Not a correct input {user_name}. Try again. "))
    else:
        if integer %2 != 0 and integer < 60:
                print(f"{user_name} {integer} is Odd and less than 60")
        elif integer %2 == 0 and integer >= 2 and integer < 25:
                print(f"{user_name} {integer} is Even and less than 25.")
        elif integer %2 == 0 and integer >= 26 and integer < 61:
                print(f"{user_name} {integer} is Even and between 26 and 60 inclusive.")
        elif integer %2 == 0 and integer > 60:
                print(f"{user_name} {integer} is Even and greater than 60.")
        elif integer %2 != 0 and integer > 60:
                print(f"{user_name} {integer} is Odd and greater than 60.")
        playing = input("Do you want to play again? ")