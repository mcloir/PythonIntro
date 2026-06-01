classA = {"Ana", "Beatriz", "Cláudio", "Daniel"}
classB = {"Ana", "Eduardo", "Felipe", "Diana"}

# Union
all = classA | classB
print(all)

# Intersection
commons = classA & classB
print(commons)

# Difference
onlyA = classA - classB
print(onlyA)

# Symmetric Difference - name in only one class
exclusive = classA ^ classB
print(exclusive)