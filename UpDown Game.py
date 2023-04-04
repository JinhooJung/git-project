answer = 14

for i in range (0, 10):
    value = input()
    value = int(value)

    if answer == value:
        print("Correct")
        break
    elif answer > value:
        print("UP")
    elif answer < value:
        print("DOWN")

    if i == 9:
        print("\nYou Fail")

