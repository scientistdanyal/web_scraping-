import pdfplumber
import re
import csv
import glob
import os

# Define a function to extract information from a PDF
def extract_information(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    # Define regular expressions for extracting data
    name_pattern = r'([A-Z][a-z]+) ([A-Z][a-z]+)'
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    email_pattern = r'\S+@\S+'

    # Extract information using regular expressions
    name_match = re.search(name_pattern, text)
    phone_numbers = re.findall(phone_pattern, text)
    email_addresses = re.findall(email_pattern, text)

    # Initialize data variables
    first_name = ""
    last_name = ""
    phone_number = ""
    email = ""
    city = ""
    state = ""
    zip_code = ""

    # Check if regex matches
    if name_match:
        first_name, last_name = name_match.groups()
    if phone_numbers:
        # Select the phone number from the second line
        phone_number = phone_numbers[1] if len(phone_numbers) > 1 else phone_numbers[0]
    if email_addresses:
        email = email_addresses[0]

    # Split the text into lines
    lines = text.split('\n')
    location_pattern = r'New ([A-Z][a-z\s,]+)\s*([A-Z]{2})\s*\((\d{5})\)\s*([A-Z]+)'
    for line in lines:
        location_match = re.search(location_pattern, line)
        if location_match:
            city, state, zip_code, country = location_match.groups()
            break
    print([first_name, last_name, phone_number, email, city, state, zip_code])
    return [first_name, last_name, phone_number, email, city, state, zip_code]

# Path to the folder containing PDF files
pdf_folder = 'data/'

# Get a list of all PDF files in the folder
pdf_files = glob.glob(os.path.join(pdf_folder, '*.pdf'))

# Create and open a CSV file for writing
with open('resume_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write header row
    csv_writer.writerow(['First Name', 'Last Name', 'Phone Number', 'Email', 'City', 'State', 'Zip Code'])

    # Iterate through PDF files and extract information
    for pdf_file in pdf_files:
        data = extract_information(pdf_file)
        csv_writer.writerow(data)

print("Data extraction and saving to CSV completed.")
