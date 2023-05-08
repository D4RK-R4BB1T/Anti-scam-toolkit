import hashlib
import os
import requests
import stem.process
import sys

def install_libraries():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "hashlib", "requests", "stem"])
        print("Libraries installed successfully.")

    except subprocess.CalledProcessError:
        print("Failed to install libraries. Please make sure you have pip installed.")
        sys.exit(1)

def install_tor():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "stem"])
        print("Tor installed successfully.")

    except subprocess.CalledProcessError:
        print("Failed to install Tor. Please make sure you have pip installed.")
        sys.exit(1)

def configure_tor():
    try:
        tor_process = stem.process.launch_tor()
        print("Tor started successfully.")
        return tor_process

    except stem.SocketError:
        print("Tor not found. Installing Tor...")
        install_tor()
        print("Tor installed successfully.")
        return configure_tor()

def download_file(url, filename):
    try:
        response = requests.get(url, stream=True)

        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print("File downloaded successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to download file - {str(e)}")

def download_hidden_service_html(url):
    tor_process = configure_tor()
    with tor_process:
        try:
            hidden_service_url = url + ".onion"
            response = requests.get(hidden_service_url)
            if response.status_code == 200:
                filename = url.split("/")[-1] + ".html"
                with open(filename, "w") as file:
                    file.write(response.text)
                print("HTML file downloaded successfully.")
            else:
                print("Error: Failed to access hidden service HTML.")
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to access hidden service - {str(e)}")

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

# Option 1: Download HTML file from Tor hidden service
url = input("Enter the URL of the Tor hidden service (without .onion): ")
download_hidden_service_html(url)

# Option 2: Download favicon.ico from Tor hidden service
url = input("Enter the URL of the Tor hidden service favicon.ico: ")
filename = input("Enter the filename for the downloaded favicon.ico: ")
download_file(url, filename)
