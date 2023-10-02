def string_operations():
    original_str = "Python Programming"

    # Extract "Python" using index slicing
    sub1 = original_str[:6]

    # Extract "Programming" using index slicing
    sub2 = original_str[7:]

    # Merge the substrings using concatenation
    merged_str = sub2 + " " + sub1  # Corrected the variable name

    print("Original String:", original_str)
    print("Extracted Substring 1:", sub1)
    print("Extracted Substring 2:", sub2)
    print("Merged String:", merged_str)  # Corrected the variable name

if __name__ == '__main__':
    string_operations() 
