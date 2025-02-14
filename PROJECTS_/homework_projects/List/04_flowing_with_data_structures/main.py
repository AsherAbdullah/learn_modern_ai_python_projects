def add_three_copies(lst, data):
    """Adds three copies of data to the given list (mutates the list)."""
    lst.append(data)
    lst.append(data)
    lst.append(data)

# Running the program
if __name__ == "__main__":
    message = input("Enter a message to copy: ")

    my_list = []  # Empty list before mutation
    print("\nList before:", my_list)

    add_three_copies(my_list, message)

    print("List after:", my_list)
