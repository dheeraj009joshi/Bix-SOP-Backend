import json
import re
import PyPDF2
import pdfplumber
import pytesseract
from PIL import Image

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to extract text from an image file
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Function to parse the extracted text and find key information
def parse_bill_data(text):
    # Example: Extracting date, amount, and invoice number using regex
    data = {}
    data['date'] = re.search(r'\b\d{2}/\d{2}/\d{4}\b', text)  # MM/DD/YYYY
    data['amount'] = re.search(r'\$\d+(?:,\d{3})*(?:\.\d{2})?', text)  # Amount in $ format
    data['invoice_number'] = re.search(r'Invoice\s*#\s*(\w+)', text)  # Extracting Invoice Number
    
    # If matches found, extract text otherwise set as None
    data['date'] = data['date'].group() if data['date'] else None
    data['amount'] = data['amount'].group() if data['amount'] else None
    data['invoice_number'] = data['invoice_number'].group(1) if data['invoice_number'] else None
    
    return data

# Main function to handle file processing and JSON storage
def process_bill(file_path, file_type):
    if file_type == 'pdf':
        text = extract_text_from_pdf(file_path)
    elif file_type == 'image':
        text = extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file type")

    # Parse the bill data
    bill_data = parse_bill_data(text)
    
    # Save the extracted data to a JSON file
    with open('bill_data.json', 'w') as json_file:
        json.dump(bill_data, json_file, indent=4)
    
    print("Data extracted and saved to bill_data.json")

# Example usage
if __name__ == "__main__":
    pdf_file_path = 'path_to_pdf_file.pdf'
    image_file_path = 'bill1.jpeg'
    
    # Process PDF
    # process_bill(pdf_file_path, 'pdf')
    
    # Process Image
    process_bill(image_file_path, 'image')
