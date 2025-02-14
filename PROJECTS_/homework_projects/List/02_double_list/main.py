def double_numbers(numbers):
    """Returns a new list with each number doubled."""
    return [num * 2 for num in numbers]

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],       # Expected output: [2, 4, 6, 8]
        [5, 10, 15],        # Expected output: [10, 20, 30]
        [0, -1, -2, 7],     # Expected output: [0, -2, -4, 14]
        [100, 200, 300],    # Expected output: [200, 400, 600]
    ]

    for case in test_cases:
        doubled = double_numbers(case)
        print(f"Original: {case} -> Doubled: {doubled}")

