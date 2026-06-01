# 1. Define a function that takes a list named 'grades' as a parameter
def calc_average(grades):
    # 2. Defensive programming: Check if the list is empty
    # If 'grades' is empty, 'sum' and 'len' would cause an error (division by zero)
    if not grades:
        return 0
    
    # 3. Calculate the average using built-in functions
    # sum(grades) adds all numbers, len(grades) counts the items
    return sum(grades) / len(grades)

def def_performance(average):
    if average >= 8.5:
        return "Excellent"
    elif average >= 7:
        return "Good"
    elif average >= 6:
        return "Average"
    else:
        return "Poor"

# 4. Create a list of numbers
grades = [7.5, 8.6, 8.7, 9]

# 5. Call the function and store the result in a variable
average = calc_average(grades)

# 6. Display the final result using an f-string
print(f"The average is {average}")

print(f"Your performance is {def_performance(average)}")