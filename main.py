def print_pattern():
    n = int(input("Enter the number of rows for the pattern: "))
    for i in range(n, 0, -1):
        print("* " * i)

def rotate_array():
    n = int(input("Enter the number of elements in the array: "))
    k = int(input("Enter the number of steps to rotate: "))
    array = [int(x) for x in input("Enter the array elements separated by space: ").split()]
    k = k % n  # Ensure k is within the array size
    rotated_array = array[-k:] + array[:-k]
    print("Rotated array:", rotated_array)

def display_help():
    print("--- Help ---")
    print("Option 1: Print a pattern with 'n' rows of decreasing asterisks.")
    print("Option 2: Rotate an array of 'n' elements to the right by 'k' steps.")
    print("Option 3: Display this help message.")
    print("Option 4: Exit the program")

while True:
    print("Welcome to the Menu-Based Program!")
    print("Please select an option:")
    print("1. Print Pattern")
    print("2. Rotate Array")
    print("3. Help")
    print("4. Exit")

    option = int(input("Option: "))

    if option == 1:
        print_pattern()
    elif option == 2:
        rotate_array()
    elif option == 3:
        display_help()
    elif option == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option (1-4).")
