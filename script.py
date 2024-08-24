import time
import random
import threading
import os
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Ask for city and keyword inputs
city = input("Enter the city name: ").replace(' ', '-')
keyword = input("Enter the search keyword: ").replace(' ', '-')

# Generate URL based on inputs
base_url = "https://www.justdial.com/"
url = f"{base_url}{city}/{keyword}/"

# Set up Chrome options
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Hide WebDriver signature
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

def check_and_click_close_popup(driver):
    """Check for the close popup button and click it if found."""
    try:
        close_popup_button = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'jd_modal_close'))
        )
        if close_popup_button.is_displayed():
            close_popup_button.click()
            print("Clicked 'jd_modal_close' button.")
            return True
    except:
        pass  # Silence the exception and avoid printing the error message
    return False

def countdown_timer(seconds):
    """Display a countdown timer in the console."""
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds", end='\r')
        time.sleep(1)
    print("Time's up! Stop file will be created.")
    with open('stop.txt', 'w') as f:
        f.write('')

# Start the countdown timer in a separate thread
countdown_thread = threading.Thread(target=countdown_timer, args=(300,))
countdown_thread.start()

def smooth_scroll_to(driver, target_position, duration=2):
    """Smoothly scroll the page to a target position."""
    start_position = driver.execute_script("return window.pageYOffset")
    distance = target_position - start_position
    start_time = time.time()
    
    while time.time() - start_time < duration:
        elapsed_time = time.time() - start_time
        scroll_position = start_position + (distance * (elapsed_time / duration))
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(0.1)  # Adjust sleep time for smoother scrolling

    # Ensure we end exactly at the target position
    driver.execute_script(f"window.scrollTo(0, {target_position});")

def human_like_scroll(driver, min_scroll_down=8, max_scroll_down=10, min_scroll_up=2, max_scroll_up=5, scroll_pause_range=(1, 2), stop_file='stop.txt'):
    last_height = driver.execute_script("return document.body.scrollHeight")
    last_position = driver.execute_script("return window.pageYOffset")  # Store the last scroll position
    last_content_check_time = time.time()  # Set to current time
    content_check_interval = 5  # Time in seconds to check if new content is loaded

    while True:  # Infinite loop for continuous scrolling
        # Scrolling Down Phase
        total_scroll_down = random.randint(min_scroll_down, max_scroll_down)
        scroll_down_count = 0
        while scroll_down_count < total_scroll_down:
            # Check if stop file exists
            if os.path.exists(stop_file):
                print("Stop file detected. Stopping scroll.")
                return  # Exit the function and stop scrolling

            driver.execute_script("window.scrollBy(0, window.innerHeight / 2);")
            scroll_down_count += 1
            print(f"Scrolling down, attempt {scroll_down_count}/{total_scroll_down}")

            # Check and handle the popup button
            check_and_click_close_popup(driver)

            time.sleep(random.uniform(*scroll_pause_range))

            # Check if new content is loaded
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height != last_height:
                print("New content detected.")
                last_height = new_height  # Update last_height if new content is loaded
                scroll_down_count = 0  # Reset scroll down counter when new content is detected
                last_content_check_time = time.time()  # Update the content check time
                last_position = driver.execute_script("return window.pageYOffset")  # Update last known position

        # Scrolling Up Phase (only if new content was detected)
        total_scroll_up = random.randint(min_scroll_up, max_scroll_up)
        scroll_up_count = 0
        while scroll_up_count < total_scroll_up:
            # Check if stop file exists
            if os.path.exists(stop_file):
                print("Stop file detected. Stopping scroll.")
                return  # Exit the function and stop scrolling

            driver.execute_script("window.scrollBy(0, -window.innerHeight / 2);")
            scroll_up_count += 1
            print(f"Scrolling up, attempt {scroll_up_count}/{total_scroll_up}")

            # Check and handle the popup button
            check_and_click_close_popup(driver)

            time.sleep(random.uniform(*scroll_pause_range))

            # Check if new content is loaded
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height != last_height:
                print("New content detected.")
                last_height = new_height  # Update last_height if new content is loaded
                scroll_up_count = 0  # Reset scroll up counter when new content is detected
                last_content_check_time = time.time()  # Update the content check time
                last_position = driver.execute_script("return window.pageYOffset")  # Update last known position

        # If no new content is detected for a long time, scroll to the top like a human, wait a bit, and scroll back to the older location
        if time.time() - last_content_check_time > content_check_interval:
            print("No new content detected for a while. Smoothly scrolling to the top.")
            smooth_scroll_to(driver, 0, duration=3)  # Smoothly scroll to the top in 3 seconds
            time.sleep(5)  # Wait for 5 seconds

            print(f"Smoothly scrolling back to last known position: {last_position}")
            smooth_scroll_to(driver, last_position, duration=3)  # Smoothly scroll back to the last position in 3 seconds

            last_content_check_time = time.time()  # Reset the content check timer

try:
    driver.get(url)
    print("Opened URL:", url)

    # Check for 'Maybe Later' popup and click it if found
    time.sleep(5)
    try:
        maybe_later_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'maybelater'))
        )
        if maybe_later_button.is_displayed():
            maybe_later_button.click()
            print("Clicked 'Maybe Later' button.")
    except Exception as e:
        print(f"Maybe Later popup not found or failed to click: {str(e)}")

    human_like_scroll(driver)

    # Fetch and save page source for debugging
    page_source = driver.page_source
    with open('page_source.html', 'w', encoding='utf-8') as f:
        f.write(page_source)
    print("Page source saved to 'page_source.html'.")

    # Ensure the 'Scrapped' folder exists
    os.makedirs('Scrapped', exist_ok=True)

    # Find and save data in CSV
    csv_filename = os.path.join('Scrapped', f"{keyword}.csv")
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Address', 'Phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        parent_divs = driver.find_elements(By.CLASS_NAME, 'resultbox_info')
        if not parent_divs:
            print("No parent divs found. Check the class name and page source.")
        else:
            for index, parent_div in enumerate(parent_divs):
                try:
                    name_div = parent_div.find_element(By.CLASS_NAME, 'resultbox_title_anchor')
                    name = name_div.text.strip()
                    phone_div = parent_div.find_element(By.CLASS_NAME, 'callcontent')
                    phone_number = phone_div.text.strip()
                    address_div = parent_div.find_element(By.CLASS_NAME, 'resultbox_address')  # Updated to include address
                    address = address_div.text.strip()

                    if name and phone_number and address:
                        writer.writerow({'Name': name, 'Address': address, 'Phone': phone_number})
                    else:
                        print(f"Missing data in parent div {index}. Name: '{name}', Address: '{address}', Phone: '{phone_number}'")

                except Exception as e:
                    with open('error_log.txt', 'a', encoding='utf-8') as error_file:
                        error_file.write(f"An error occurred in parent div {index}: {str(e)}\n")

    print(f"Data extraction completed and saved to '{csv_filename}'.")

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

finally:
    # Print script completion message
    print("Script execution completed. Browser will remain open.")
    
    # Wait for 3 seconds
    time.sleep(3)
    
    # Remove page_source.html and stop.txt files
    if os.path.exists('page_source.html'):
        os.remove('page_source.html')
    if os.path.exists('stop.txt'):
        os.remove('stop.txt')
    if os.path.exists('error_log.txt'):
        os.remove('error_log.txt')
    
    # Keep the browser open, looping indefinitely until manually closed
    while True:
        time.sleep(10)
