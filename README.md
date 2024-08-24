# Web Scraper Script

This Python script automates the process of scraping contact information from a specified website using the Selenium library with Google Chrome. The script handles pop-ups, performs human-like scrolling, and extracts data like names and phone numbers.

## Features

- **Pop-up Handling**: Automatically detects and closes pop-ups that might interfere with the scraping process.
- **Human-like Scrolling**: The script scrolls the page incrementally to mimic a real user's behavior, ensuring that dynamically loaded content is captured.
- **Countdown Timer**: A countdown timer runs in a separate thread, creating a stop file after a specified time to halt the scrolling.
- **Data Extraction**: Scrapes and saves contact information (e.g., names and phone numbers) to a text file.

## Requirements

The script requires Python 3.x and the following Python packages:

- `selenium`: For automating web browser interactions.
- `webdriver_manager`: To automatically manage and download the ChromeDriver executable.

These packages are listed in the `requirements.txt` file.

## Installation

### 1. Clone the Repository and Install Requirements

First, clone the repository to your local machine and install the required packages:

```sh
git clone https://github.com/r7avi/JustDial-Data-Scrapper.git
cd Just Dail Scrapper
pip install -r requirements.txt


### Summary:
- **Installation Instructions**: Consolidated into a single step that includes cloning the repository and installing the requirements.
- **Execution**: Clear, concise instructions for running the script.

This approach keeps the `README.md` streamlined and user-friendly.
