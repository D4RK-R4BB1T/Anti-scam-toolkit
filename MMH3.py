import mmh3
import hashlib

# Prompt the user to input the file path
file_path = input("Enter the path to the HTML file: ")

try:
    # Read the contents of the HTML file
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # Calculate the MMH3 hash
    mmh3_hash = mmh3.hash(file_content)

    # Calculate the hexadecimal hash
    hex_hash = hashlib.md5(file_content).hexdigest()

    # Print the hashes
    print("MMH3 Hash:", mmh3_hash)
    print("Hexadecimal Hash:", hex_hash)

except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
