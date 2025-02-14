def fahrenheit_to_celsius(degrees_fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (degrees_fahrenheit - 32) * 5.0 / 9.0

# Test cases
if __name__ == "__main__":
    test_cases = [76.0, 32.0, 100.0, 0.0, -40.0]
    
    for temp in test_cases:
        converted = fahrenheit_to_celsius(temp)
        print(f"Temperature: {temp}F = {converted}C")
