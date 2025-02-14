def calculate_sum(num1, num2):
    return num1 + num2

# Test cases
if __name__ == "__main__":
    test_cases = [
        (5, 10),
        (-3, 7),
        (0, 0),
        (100, 200)
    ]
    
    for num1, num2 in test_cases:
        result = calculate_sum(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}.")
