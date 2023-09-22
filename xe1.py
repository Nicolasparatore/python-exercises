# Input a binary number as a string (with or without '0b' prefix)
binary_number = input("Enter a binary number: ")

# Remove the '0b' prefix if it exists
binary_number = binary_number.replace('0b', '')

# Use the int() function to convert to decimal
decimal_representation = int(binary_number, 2)

# Print the result
print("Decimal representation:", decimal_representation)