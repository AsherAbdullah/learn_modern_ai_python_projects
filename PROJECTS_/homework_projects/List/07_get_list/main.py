def collect_values():
    """Continuously collects values from the user until they press enter without input."""
    user_list = []
    
    while True:
        value = input("Enter a value: ")
        if value == "":  # Stop when the user presses enter without typing anything
            break
        user_list.append(value)

    print("\nHere's the list:", user_list)

# Run the program
if __name__ == "__main__":
    collect_values()
