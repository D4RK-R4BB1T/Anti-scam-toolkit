Certainly! Here's the updated version of the script that includes the requested functionality:

```python
import mmh3
import hashlib
import requests
import os
import subprocess
import sys


def install_libraries():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "mmh3", "hashlib"])
        print("Libraries installed successfully.")

    except subprocess.CalledProcessError:
        print("Failed to install libraries. Please make sure you have pip installed.")
        sys.exit(1)


def calculate_file_hash(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()

        mmh3_hash = mmh3.hash(file_content)
        hex_hash = hashlib.md5(file_content).hexdigest()

        print("MMH3 Hash:", mmh3_hash)
        print("Hexadecimal Hash:", hex_hash)

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")


def download_file(url, file_extension):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_content = response.content

            file_name = "downloaded_file" + file_extension
            with open(file_name, 'wb') as file:
                file.write(file_content)

            print("File downloaded successfully as", file_name)
            calculate_file_hash(file_name)

        else:
            print("Failed to download file. Invalid URL or resource not found.")

    except requests.exceptions.RequestException:
        print("Failed to download file. Connection error.")


def clone_github_repo(repo_url):
    try:
        subprocess.run(["git", "clone", repo_url])

        repo_name = repo_url.split("/")[-1].rstrip(".git")
        print("Repository cloned successfully as", repo_name)

        file_path = input("Enter the path to the file you want to generate a hash from: ")

        extension = os.path.splitext(file_path)[1].lower()
        if extension == ".html" or extension == ".ico":
            calculate_file_hash(file_path)
        else:
            print("Unsupported file extension. Only HTML and .ico files are supported.")

    except subprocess.CalledProcessError:
        print("Failed to clone the repository. Invalid URL or permission denied.")


# Check if the required libraries are installed
try:
    import mmh3
    import hashlib
    import requests
except ImportError:
    print("Required libraries not found.")

    while True:
        choice = input("Do you want to install the required libraries? (y/n): ")

        if choice.lower() == "y":
            install_libraries()
            break
        elif choice.lower() == "n":
            print("Cannot proceed without the required libraries. Exiting.")
            sys.exit(1)
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


# Main menu
while True:
    print("---- Main Menu ----")
    print("1. Generate the hash of a local file (.html or .ico)")
    print("2. Download a .ico file or .html file from a website")
    print("3. Clone a GitHub repository")

    choice = input("Select an option (1, 2, 3), or enter 'q' to quit: ")

    if choice == "1":
        file_path = input("Enter the path to the file: ")
        calculate_file_hash(file_path)

    elif choice == "2":
        url = input("Enter the URL of the website: ")
        file_extension = input("Enter the file extension (.ico or .html): ")

           if file_extension.lower() not in [".ico", ".html"]:
            print("Invalid file extension. Only .ico and .html files are supported.")
        else:
            download_file(url, file_extension)

    elif choice == "3":
        repo_url = input("Enter the GitHub repository URL: ")
        clone_github_repo(repo_url)

    elif choice.lower() == "q":
        break

    else:
        print("Invalid choice. Please select a valid option.")
