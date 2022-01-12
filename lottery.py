def lottery():

    import random

    n1 = int(input("Enter 1st number: "))
    n2 = input("Enter 2nd number: ")
    n3 = input("Enter 3rd number: ")

    num1 = random.randrange(0, 9)
    num2 = random.randrange(0, 9)
    num3 = random.randrange(0, 9)

    print(f"Lottery numbers: {num1} {num2} {num3}")

    if n1 == num1 and n2 == num2 and n3 == num3:
        print("Winner!")
    if n1 == num1 and n2 == num3 and n3 == num2:
        print("Winner!")
    if n1 == num2 and n2 == num1 and n3 == num3:
        print("Winner!")
    if n1 == num2 and n2 == num3 and n3 == num1:
        print("Winner!")
    if n1 == num3 and n2 == num1 and n3 == num2:
        print("Winner!")
    if n1 == num3 and n2 == num2 and n3 == num1:
        print("Winner!")
    else:
        print("You lose.")

    retry = input("Would you like to try again? (y/n): ")
    if retry == "y":
        lottery()
    else:
        exit()

lottery()