def feet_to_inches(feet):
    """Converts feet to inches (1 foot = 12 inches)."""
    return feet * 12

# Running the program with user input
if __name__ == "__main__":
    try:
        feet = float(input("Enter the number of feet: "))
        inches = feet_to_inches(feet)
        unit = "foot" if feet == 1 else "feet"
        print(f"{feet} {unit} is equal to {inches} inches.")
    except ValueError:
        print("Please enter a valid numerical value for feet.")
