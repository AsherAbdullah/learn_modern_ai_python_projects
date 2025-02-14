def calculate_perimeter(side1, side2, side3):
    """Calculates the perimeter of a triangle given its three sides."""
    return side1 + side2 + side3

# Test cases
if __name__ == "__main__":
    test_cases = [
        (3, 4, 5.5),
        (7, 10, 5),
        (6.5, 6.5, 6.5),
        (2.3, 3.1, 4.8)
    ]
    
    for sides in test_cases:
        perimeter = calculate_perimeter(*sides)
        print(f"The perimeter of the triangle with sides {sides} is {perimeter}")
