def square_number(number):
    return number ** 2

# Test cases
if __name__ == "__main__":
    test_cases = [2, 4, 5.5, 10, -3]
    
    for num in test_cases:
        squared = square_number(num)
        print(f"{num} squared is {squared}")