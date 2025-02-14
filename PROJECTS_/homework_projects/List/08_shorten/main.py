MAX_LENGTH = 3  # The maximum allowed length of the list

def shorten(lst):
    """Removes elements from the end of lst until its length is MAX_LENGTH."""
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Removes the last element
        print("Removed:", removed_item)

    print("\nFinal list:", lst)

# Running the program
if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))

    user_list = []
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    print("\nOriginal List:", user_list)
    shorten(user_list)
