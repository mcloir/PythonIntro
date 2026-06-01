compras = [] # empty list
grades = [7.5, 8.6, 8.7, 9] # non empty list
dados = ["Alice in Chains", 14, 1.77, True] # mixed types list
numbers = list(range(1, 5)) # [1, 2, 3, 4]

average = sum(grades) / len(grades)

print(grades)
print(sum(grades))
print(len(grades))
print(average)

lowgrades = [grade for grade in grades if grade < 8]
# grade (at the start): This is the expression. It tells Python what to add to the new list. In this case, it just adds the value of grade itself (no modifications).
# for grade in grades: This is the loop that iterates through every item in your original list called grades. Each individual item is temporarily assigned to the variable grade.
# if grade < 8: This is the filter. It checks each grade to see if it meets the condition (being less than 8). If the condition is False, that item is skipped.
print(lowgrades)