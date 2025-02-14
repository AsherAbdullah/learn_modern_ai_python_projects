def sum_of_numbers(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],       # Expected output: 15
        [10, -2, 8, 3],        # Expected output: 19
        [0, 0, 0, 0],          # Expected output: 0
        [100, 200, 300],       # Expected output: 600
        [-5, -10, -15]         # Expected output: -30
    ]

    for case in test_cases:
        print(f"Sum of {case} is {sum_of_numbers(case)}")

