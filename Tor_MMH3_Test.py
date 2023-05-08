import hashlib
import os
import requests
import stem.process
import stem.util.log
import sys
import subprocess

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

def is_tor_running():
    try:
        socks_port = stem.util.log.get_localhost().find_free_port()
        control_port = stem.util.log.get_localhost().find_free_port()
        tor_process = stem.process.launch_tor_with_config(
            config={
                'SocksPort': str(socks_port),
                'ControlPort': str(control_port),
            },
            take_ownership=True
        )
        tor_process.kill()
        return True

    except stem.SocketError:
        return False

def start_tor():
    try:
        tor_process = stem.process.launch_tor()
        print("Tor started successfully.")
        return tor_process

    except stem.SocketError:
        print("Failed to start Tor. Please make sure Tor is installed properly.")
        sys.exit(1)

def calculate_hash(data, algorithm):
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(data)
    return hash_obj.hexdigest()

def download_hidden_service_html(url):
    if not url.endswith(".onion"):
        print("Error: Invalid hidden service URL.")
        return

    if not is_tor_running():
        print("Tor is not running. Starting Tor...")
        tor_process = start_tor()
    else:
        print("Tor is already running.")

    with tor_process:
        try:
            hidden_service_url = url + ".onion"
            response = requests.get(hidden_service_url)
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

# Check if Tor is running or start it if necessary
if not is_tor_running():
    print("Tor is not running. Starting Tor...")
    tor_process = start_tor()
else:
    print("Tor is already running.")

# Option 1: Download HTML file from Tor hidden service
url = input("Enter the URL of the Tor hidden service (without .onion): ")
download_hidden_service_html(url)

# Option 2: Download favicon.ico from Tor hidden service
url = input("Enter the URL of the Tor hidden service favicon.ico: ")
filename = input("Enter the filename for the downloaded favicon.ico: ")
download_file(url, filename)
