list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenlist = []

for num in list:
    if num % 2 != 0:
        continue # do not consider the odd numbers
    evenlist.append(num)
print(f"The even numbers are: {evenlist}")