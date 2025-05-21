# sum_even_numbers.py

def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# Example usage
sample_list = [1, 2, 3, 4, 5, 6]
print("Sum of even numbers:", sum_even(sample_list))
