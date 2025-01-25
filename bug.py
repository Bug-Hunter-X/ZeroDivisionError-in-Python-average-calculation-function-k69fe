def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    return sum(numbers) / len(numbers)

# Incorrect usage leading to ZeroDivisionError
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Correct usage
my_numbers = [10, 20, 30]
average = calculate_average(my_numbers)
print(f"The average is: {average}")