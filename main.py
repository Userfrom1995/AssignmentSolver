import pytesseract
from PIL import Image
import io
# import PdfReader
import PyPDF2

# Path to the Tesseract executable (change this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_image(image):
    # Open the image file using PIL (Python Imaging Library)
    img = Image.open(io.BytesIO(image))

    # Perform OCR on the image using pytesseract
    extracted_text = pytesseract.image_to_string(img)

    return extracted_text

def ocr_pdf(pdf):
    # Open the PDF file using PyPDF2
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf))
    num_pages = len(pdf_reader.pages)

    extracted_text = ""

    # Extract text from each page of the PDF
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        extracted_text += page.extract_text()

    return extracted_text

# Example usage
if __name__ == "__main__":
    # Example input image file path
    # input_file_path = 'example_image.jpg'

    # Example input PDF file path
    # input_file_path = 'example_pdf.pdf'

    # Read input file
    input_file_path = input("Enter the path to the input file (image or PDF): ")
    with open(input_file_path, 'rb') as file:
        file_content = file.read()

    # Perform OCR based on file type
    if input_file_path.lower().endswith('.jpg') or input_file_path.lower().endswith('.jpeg') or input_file_path.lower().endswith('.png'):
        extracted_text = ocr_image(file_content)
    elif input_file_path.lower().endswith('.pdf'):
        extracted_text = ocr_pdf(file_content)
    else:
        print("Unsupported file format. Please provide an image (JPEG/PNG) or PDF file.")

    # Print the extracted text
    print("Extracted Text:")
    print(extracted_text)
