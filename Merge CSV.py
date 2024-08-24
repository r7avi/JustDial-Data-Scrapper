import pandas as pd
import os

# Paths relative to the current working directory (Scrapped)
folder_path = 'Scrapped'  # Current directory (Scrapped)
output_folder = 'Clean Data'  # Parent directory + Clean Data folder

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

print(f'Combined data contains {len(all_data)} rows before deduplication.')

# Remove exact duplicate rows
print('Removing exact duplicate rows...')
all_data.drop_duplicates(keep='first', inplace=True)

print(f'Combined data contains {len(all_data)} rows after deduplication.')

# Save the combined data to a new CSV file in the Clean Data folder
output_file = os.path.join(output_folder, 'combined_data.csv')
print(f'Saving combined data to {output_file}...')
all_data.to_csv(output_file, index=False)

print(f'Combined data saved to {output_file}')

# Pause execution so the user can see the output
input('Press Enter to exit...')
