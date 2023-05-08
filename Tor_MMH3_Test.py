
import hashlib
import requests
import os
import subprocess
import sys
import stem.process


def install_libraries():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "hashlib", "stem"])
        print("Libraries installed successfully.")

    except subprocess.CalledProcessError:
        print("Failed to install libraries. Please make sure you have pip installed.")
        sys.exit(1)


def calculate_file_hash(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()

        mmh3_hash = hashlib.mmh3(file_content)
        sha1_hash = hashlib.sha1(file_content).hexdigest()
        sha256_hash = hashlib.sha256(file_content).hexdigest()
        sha512_hash = hashlib.sha512(file_content).hexdigest()

        print("MMH3 Hash:", mmh3_hash)
        print("SHA1 Hash:", sha1_hash)
        print("SHA256 Hash:", sha256_hash)
        print("SHA512 Hash:", sha512_hash)

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


def configure_tor():
    try:
        tor_process = stem.process.launch_tor_with_config(
            config={
                'SocksPort': '9050',
                'ControlPort': '9051',
                'Log': 'notice stdout',
            },
            tor_cmd='tor'
        )
        print("Tor configured successfully.")
        return tor_process

    except stem.SocketError:
        print("Tor not found. Please install Tor from https://www.torproject.org/")
        sys.exit(1)


# Check if the required libraries are installed
try:
    import hashlib
    import requests
    import stem.process
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


# Configure Tor
tor_process = configure_tor()

# Main menu
while True:
    print("---- Main Menu ----")
    print("1. Download and calculate hashes of a file")
    print("2. Quit")

    choice = input("Select an option (1 or 2): ")

    if choice == "1":
        file_url = input("Enter the URL of the file to download: ")
        download_file(file_url, os.path.splitext(file_url)[1])

    elif choice == "2":
        break

    else:
        print("Invalid choice. Please select a valid option.")

# Stop the Tor process
tor_process.kill()

