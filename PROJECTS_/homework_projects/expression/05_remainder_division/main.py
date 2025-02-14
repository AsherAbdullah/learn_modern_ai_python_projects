def divide_numbers(dividend, divisor):
    """Returns the quotient and remainder of the division."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Running the program with user input
if __name__ == "__main__":
    try:
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))

        if divisor == 0:
            print("Division by zero is not allowed.")
        else:
            quotient, remainder = divide_numbers(dividend, divisor)
            print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")
    except ValueError:
        print("Please enter valid integer values.")
