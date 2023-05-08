import hashlib
import os
import requests
import sys
import subprocess

def calculate_hash(data, algorithm):
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(data)
    return hash_obj.hexdigest()

def download_hidden_service_html(url):
    if not url.endswith(".onion"):
        print("Error: Invalid hidden service URL.")
        return

    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = url.split("/")[-1] + ".html"
            with open(filename, "w") as file:
                file.write(response.text)
            print("HTML file downloaded successfully.")

            # Generate Shodan link
            html_hash = calculate_hash(response.content, "md5")
            shodan_link = f"https://www.shodan.io/search?query=http.html_hash%3A{html_hash}"
            print("Shodan Link:", shodan_link)

        else:
            print("Error: Failed to access hidden service HTML.")
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to access hidden service - {str(e)}")

# Check if Tor is running or start it if necessary
def is_tor_running():
    try:
        response = subprocess.check_output(["pgrep", "-f", "tor"])
        return True
    except subprocess.CalledProcessError:
        return False

def start_tor():
    try:
        subprocess.call(["tor"])
        print("Tor started successfully.")
    except subprocess.CalledProcessError:
        print("Failed to start Tor. Please make sure Tor is installed properly.")
        sys.exit(1)

while True:
    choice = input("Do you have Tor installed and running? (y/n): ")
    if choice.lower() == "y":
        break
    elif choice.lower() == "n":
        print("Please install Tor and make sure it is running before running this script.")
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
