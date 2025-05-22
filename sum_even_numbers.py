# sum_even_numbers.py

def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# Example usage
sample_list = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16]
print("List", sample_list)
print("Sum of even numbers:", sum_even(sample_list))
