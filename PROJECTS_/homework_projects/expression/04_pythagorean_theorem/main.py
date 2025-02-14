import math

def calculate_hypotenuse(a, b):
    """Calculates the hypotenuse using the Pythagorean theorem: c² = a² + b²"""
    return math.sqrt(a**2 + b**2)

# Running the program with user input
if __name__ == "__main__":
    try:
        a = float(input("Enter the length of AB: "))
        b = float(input("Enter the length of AC: "))
        hypotenuse = calculate_hypotenuse(a, b)
        print(f"\nThe length of BC (the hypotenuse) is: {hypotenuse}")
    except ValueError:
        print("Please enter valid numerical values for the sides.")
