# creating sets
numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue"}
emptyset = set() # empty set; if using {}, it creates a empty dictionary.

print(numbers)
print(colors)
print(emptyset)

numbers.add(6)
print(numbers)

numbers.remove(3)
print(numbers)

colors.remove("red") # remove generate error if the element does not exist.
print(colors)

colors.discard("red") # discard does not generate error if the element does not exist.
print(colors)

colors.discard("green") # discard does not generate error if the element does not exist.
print(colors)

print(numbers)
if 2 in numbers:
    print("2 is in the set")
else:
    print("2 is not in the set")