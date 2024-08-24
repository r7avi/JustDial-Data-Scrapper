import subprocess
import os

def get_urls_from_file(filename):
    # Read URLs from the specified file
    try:
        with open(filename, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
            if urls:
                return urls
            else:
                print(f"The file '{filename}' is empty. Exiting.")
                exit()
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist. Exiting.")
        exit()

def run_main_py_with_url(url):
    # Write the URL to a temporary file for main.py to read
    with open('temp_url.txt', 'w') as file:
        file.write(url)
    
    # Run main.py
    subprocess.run(['python', 'main.py'], check=True)
    
    # Clean up
    if os.path.exists('temp_url.txt'):
        os.remove('temp_url.txt')

# Read URLs from URL.txt
urls = get_urls_from_file('public/assets/URL.txt')

# Run main.py for each URL
for url in urls:
    print(f"Processing URL: {url}")
    run_main_py_with_url(url)
    print(f"Finished processing URL: {url}")

print("All URLs have been processed.")
