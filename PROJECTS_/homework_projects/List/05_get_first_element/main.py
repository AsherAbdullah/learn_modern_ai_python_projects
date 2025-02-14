def get_first_element(lst):
    """Prints the first element of a non-empty list."""
    print("First element:", lst[0])

# Running the program
if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))

    user_list = []
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    print("\nUser List:", user_list)
    get_first_element(user_list)
