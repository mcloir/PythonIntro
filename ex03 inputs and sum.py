sum = 0

while True:
    num = int(input("Please input a integer to sum or type 0 to exit: "))
    if num == 0:
        break
    sum = sum + num
print("The sum of the number is: ", sum)