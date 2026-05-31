sum = 0
while True:
    try:
        num = int(input("Input a number or type 0 to exit: "))
        if num == 0:
            break
        sum += num

    except ValueError:
        print("Invalid input. Try again.")
print("The sum of numbers is ", sum)