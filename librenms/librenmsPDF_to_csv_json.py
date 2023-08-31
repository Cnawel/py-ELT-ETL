import PyPDF2
import csv
import json

'''
It opens the PDF file specified by pdf_file_path.
It reads each page of the PDF, extracts the text, and splits it into rows.
For each row, it splits the content into four fields (id, equip, severity, date).
It appends the data as dictionaries to the data list.
It defines output file paths for CSV (csv_file_path) and JSON (json_file_path).
It writes the data to a CSV file using the csv library, and to a JSON file using the json library.
Finally, it prints a message indicating where the data was saved.
'''
# Define the PDF file path
pdf_file_path = 'LibreNMS_output.pdf'

# Create empty lists to store data
data = []

# Open the PDF file for reading
with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Iterate through each page of the PDF
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)

        # Extract text from the page
        page_text = page.extractText()

        # Split the page text into rows using a newline character
        rows = page_text.strip().split('\n')

        # Assuming each row has four fields (id, equip, severity, date)
        for row in rows:
            fields = row.split('/')

            # Ensure the row has all four fields
            if len(fields) == 4:
                id, equip, severity, date = fields
                data.append({
                    'id': id.strip(),
                    'equip': equip.strip(),
                    'severity': severity.strip(),
                    'date': date.strip()
                })

# Define the output file paths for CSV and JSON
csv_file_path = 'output.csv'
json_file_path = 'output.json'

# Write data to CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['id', 'equip', 'severity', 'date'])
    csv_writer.writeheader()
    csv_writer.writerows(data)

# Write data to JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f'Data extracted from PDF and saved to {csv_file_path} and {json_file_path}.')
