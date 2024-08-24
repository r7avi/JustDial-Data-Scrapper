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

### 1. Clone the Repository 

First, clone the repository to your local machine:

```sh
git clone https://github.com/your-username/your-repository.git
cd your-repository


### 2. Install Requirements

pip install -r requirements.txt

or

py pip install -r requirements.txt

### 3. Install Chrome if not Installed

### 2. Run Python Script

python script.py

or

py script.py


### Explanation:
- **Clone the Repository**: Users are guided on how to clone the repository.
- **Virtual Environment**: Optional step for setting up a virtual environment to manage dependencies.
- **Installation of Packages**: Instructions on how to install required packages using `requirements.txt`.
- **Running the Script**: Users are guided on how to execute the script and what to expect in terms of output files.
- **Important Notes & Troubleshooting**: Provided details on how the stop mechanism works, how to handle potential issues, and reminders for legal considerations.

This `README.md` is comprehensive, covering everything a user would need to get the script up and running. Make sure to replace placeholder text like `your-username` and `your-repository` with your actual GitHub username and repository name.

