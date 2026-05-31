for n in range(1, 101):
    if n == 50:
        break
    print(n) # prints the number from 1 to 49, when i == 50 the break do not allow the print.

for i in  range(1, 6):
    if i == 3:
        continue
    print(i) # when i reach the value of 3 the loop is passed to the next i value, not printing the value 3.

if n == 10:
    pass # the pass just allows to put the if with the condition not defined.
else:
    print("Condition not satisfied")

