import pandas as pd
import os
import time

# Paths relative to the current working directory
folder_path = 'Scrapped'  # Directory containing CSV files
output_folder = 'Clean Data'  # Directory to save cleaned data

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

print(f'Found {len(csv_files)} CSV files.')

# Create an empty DataFrame to hold all the data
all_data = pd.DataFrame()

# Read each CSV file and append it to the all_data DataFrame
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    print(f'Reading {file_path}...')
    df = pd.read_csv(file_path)
    all_data = pd.concat([all_data, df], ignore_index=True)

print(f'Combined data contains {len(all_data)} rows before processing.')

# Check if 'Name' column exists
if 'Name' not in all_data.columns:
    raise ValueError("The 'Name' column is missing from the data.")

# Remove duplicates based on the 'Name' column, keeping the first occurrence
print('Removing duplicates based on the Name column, keeping the first occurrence...')
cleaned_data = all_data.drop_duplicates(subset=['Name'], keep='first')

print(f'Cleaned data contains {len(cleaned_data)} rows after removing duplicates.')

# Save the cleaned data to a new CSV file in the Clean Data folder
output_file = os.path.join(output_folder, 'cleaned_data.csv')
print(f'Saving cleaned data to {output_file}...')
cleaned_data.to_csv(output_file, index=False)

print(f'Cleaned data saved to {output_file}')

# Wait for 5 seconds before exiting
print('Exiting in 5 seconds...')
time.sleep(5)
