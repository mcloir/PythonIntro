sum = 0
while True:
    num = int(input("Input a number or type 0 to exit: "))
    if num == 0:
        break
    sum += num #operador de atribuição composto
print("The sum of numbers is ", sum)