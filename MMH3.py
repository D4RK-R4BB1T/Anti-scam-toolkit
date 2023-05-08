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


# Check if the required libraries are installed, install them if necessary
try:
    import mmh3
    import hashlib
except ImportError:
    print("Required libraries not found. Installing libraries...")
    install_libraries()


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


# Generate the hash of a local file (.html or .ico)
file_path = input("Enter the path to the .ico or .html file: ")
calculate_file_hash(file_path)

# Download a .ico file or .html file from a website
url = input("Enter the URL of the website (supporting HTTP and HTTPS): ")
file_extension = input("Enter the file extension (.ico or .html): ")

if file_extension.lower() not in [".ico", ".html"]:
    print("Invalid file extension. Only .ico and .html files are supported.")
else:
    download_file(url, file_extension)
