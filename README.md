# Web Scraper Script

This script is designed to automate the process of scraping a specified website for contact information using the Selenium library with Google Chrome. The script also handles potential pop-ups and performs human-like scrolling to ensure content is loaded dynamically.

## Features

- **Pop-up Handling**: The script can detect and close pop-ups that might obstruct the scraping process.
- **Human-like Scrolling**: To simulate a real user, the script scrolls the page gradually, waiting for new content to load.
- **Countdown Timer**: A separate thread runs a countdown timer, which creates a stop file after a specified period, signaling the script to stop scrolling.
- **Data Extraction**: Scrapes and saves contact names and phone numbers to a text file.

## Requirements

To run this script, you need to have the following installed on your machine:

1. **Python 3.x**
2. **pip** (Python package installer)
3. **Google Chrome** browser

## Python Dependencies

Install the required Python packages using the following command:

```sh
pip install selenium webdriver_manager
