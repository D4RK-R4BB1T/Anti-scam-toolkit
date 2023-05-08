import hashlib
import ssl
import socket


def calculate_ssl_certificate_hashes(url):
    try:
        # Establish an SSL connection to the website
        context = ssl.create_default_context()
        with socket.create_connection((url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssl_sock:
                # Retrieve the SSL certificate
                cert = ssl_sock.getpeercert(binary_form=True)

        # Calculate the hashes of the SSL certificate
        sha1_hash = hashlib.sha1(cert).hexdigest()
        sha256_hash = hashlib.sha256(cert).hexdigest()
        sha512_hash = hashlib.sha512(cert).hexdigest()
        md5_hash = hashlib.md5(cert).hexdigest()
        sha3_256_hash = hashlib.sha3_256(cert).hexdigest()

        print("SHA1 Hash:", sha1_hash)
        print("SHA256 Hash:", sha256_hash)
        print("SHA512 Hash:", sha512_hash)
        print("MD5 Hash:", md5_hash)
        print("SHA3-256 Hash:", sha3_256_hash)

    except socket.gaierror:
        print("Failed to resolve the host. Please provide a valid website URL.")
    except ssl.SSLError:
        print("Failed to establish an SSL connection. Please ensure the website supports SSL.")
    except ConnectionRefusedError:
        print("Failed to connect to the website. Please check the website URL or your internet connection.")


# Main code
url = input("Enter the website URL (e.g., example.com): ")
calculate_ssl_certificate_hashes(url)
