# utils.py

import time
import random
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def human_like_scroll(driver, min_scroll_down=9, max_scroll_down=10, min_scroll_up=9, max_scroll_up=10, scroll_pause_range=(1, 2), stop_file='stop.txt'):
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
            time.sleep(3)  # Wait for 3 seconds

            print(f"Smoothly scrolling back to last known position: {last_position}")
            smooth_scroll_to(driver, last_position, duration=3)  # Smoothly scroll back to the last position in 3 seconds

            last_content_check_time = time.time()  # Reset the content check timer


