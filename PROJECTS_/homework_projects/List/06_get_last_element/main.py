def get_last_element(lst):
    """Prints the last element of a non-empty list."""
    print("Last element:", lst[-1])  # Accessing the last element using negative indexing

# Running the program
if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))

    user_list = []
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    print("\nUser List:", user_list)
    get_last_element(user_list)
