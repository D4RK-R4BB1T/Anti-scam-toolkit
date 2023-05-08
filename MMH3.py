import mmh3
import hashlib
import requests
import os
import subprocess
import sys


def calculate_file_hash(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()

        mmh3_hash = mmh3.hash(file_content)
        hex_hash = hashlib.md5(file_content).hexdigest()

        print("MMH3 Hash:", mmh3_hash)
        print("Hexadecimal Hash:", hex_hash)

        # Generate Shodan link
        shodan_link = f"https://www.shodan.io/search?query=http.html_hash%3A{mmh3_hash}"
        print("Shodan Link:", shodan_link)

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")


# Main menu
while True:
    print("---- Main Menu ----")
    print("1. Generate the hash of a local file (.html or .ico)")
    print("2. Download a .ico file or .html file from a website")
    print("3. Clone a GitHub repository")
    print("99. Exit")

    choice = input("Select an option (1, 2, 3), or enter '99' to quit: ")

    if choice == "1":
        file_path = input("Enter the path to the .ico or .html file: ")
        calculate_file_hash(file_path)

    elif choice == "2":
        url = input("Enter the URL of the website (supporting HTTP and HTTPS): ")
        file_extension = input("Enter the file extension (.ico or .html): ")

        if file_extension.lower() not in [".ico", ".html"]:
            print("Invalid file extension. Only .ico and .html files are supported.")
        else:
            # Download file and calculate hash
            response = requests.get(url)
            if response.status_code == 200:
                file_content = response.content

                # Save file locally
                file_name = "downloaded_file" + file_extension
                with open(file_name, 'wb') as file:
                    file.write(file_content)

                print("File downloaded successfully as", file_name)
                calculate_file_hash(file_name)

            else:
                print("Failed to download file. Invalid URL or resource not found.")

    elif choice == "3":
        repo_url = input("Enter the GitHub repository URL: ")
        # Clone the repository and perform desired operations
        # ...

    elif choice == "99":
        break

    else:
        print("Invalid choice. Please select a valid option.")
