for i in  range(4):
    print(i)

names = ["Alice", "Bob", "Charlie", "Daniel"]

for name in names: # name could be named by whatever you want like "i", "list", "astolfo"...
    print(f"Hello, {name}")

for n in range(1,6):
    print(f"\n---Table of {n}---")
    for m in range(1,11):
        result = n * m
        print(f"{n} x {m} = {result}")