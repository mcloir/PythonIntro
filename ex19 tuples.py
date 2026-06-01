coord = (10, 20, 30) # tuple with elements
singtuple = (10,) # tuple with one element
emptytuple = () # empty tuple
point = 3, 4 # tuple without parentesis
print(coord)
print(singtuple)
print(emptytuple)
print(point)

# 1. Define a function that returns multiple values
def rectangle_dimensions():
    dimA = 10
    dimB = 5
    # When you return two values separated by a comma, 
    # Python automatically packs them into a single tuple (10, 5)
    return dimA, dimB 

# 2. Call the function and print the result directly
# This will display the tuple: (10, 5)
print(rectangle_dimensions())

# 3. Tuple Unpacking:
# The function returns a tuple. We assign the first value (10) 
# to 'l' and the second value (5) to 'a' in a single line.
l, a = rectangle_dimensions()

# 4. Print individual variables
print(l) # Outputs: 10
print(a) # Outputs: 5

city_map = {(10, 20): "Campina Grande", (-30, 30): "João Pessoa"}
print(city_map)