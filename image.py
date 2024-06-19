# Import the required libraries
from openai import OpenAI
import pytesseract
from PIL import Image
import io
import PyPDF2
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



# Path to the Tesseract executable (change this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize the OpenAI client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def ocr_image(image):
    # Open the image file using PIL (Python Imaging Library)
    img = Image.open(io.BytesIO(image))

    # Perform OCR on the image using pytesseract
    extracted_text = pytesseract.image_to_string(img)

    return extracted_text


def save_to_pdf(text, output_file_path):
    # Create a canvas
    c = canvas.Canvas(output_file_path, pagesize=letter)

    # Set font and size
    c.setFont("Helvetica", 12)

    # Write text to PDF
    c.drawString(100, 700, text)

    # Save the PDF file
    c.save()


def save_to_word(text, output_file_path):
    # Create a new Word document
    doc = Document()

    # Add a paragraph with the text to the document
    doc.add_paragraph(text)

    # Save the Word document
    doc.save(output_file_path)


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


def classify_and_correct_text(text):
    # Pass the text to the local AI model (Lama) for classification and correction
    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=[
            {
                "role": "system",
                "content": "So the inputs I am providing you are the questions and your role is of a student and those are your assignment questions and you have to solve them since clearly with proper headings and you have to first write the question and then the answer and you have to do it with the whole assignment so you have to solve the assignment as good as possible so that your professor will give you good marks ",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": text},
                ],
            }
        ],
        max_tokens=1000,
        stream=False,
        timeout=600
    )

    class MyClass:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f"{self.value})"

    # Create an instance of the class
    obj = MyClass(completion)

    # Return the object
    return obj


# Example usage
if __name__ == "__main__":
    # Example input file path
    input_file_path = input("Enter the path to the input file (image or PDF): ")

    # Read input file
    with open(input_file_path, 'rb') as file:
        file_content = file.read()

    # Perform OCR based on file type
    if input_file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        extracted_text = ocr_image(file_content)
    elif input_file_path.lower().endswith('.pdf'):
        extracted_text = ocr_pdf(file_content)
    else:
        print("Unsupported file format. Please provide an image (JPEG/PNG) or PDF file.")

    # Print the extracted text
    print("Extracted Text:")
    print(extracted_text)

    # Classify and correct the text
    corrected_text1 = classify_and_correct_text(extracted_text)
    print(corrected_text1)

    # # Save to PDF
    # save_to_pdf(str(corrected_text1), "Answers/output.pdf")

    # Save to Word
    save_to_word(str(corrected_text1), "Answers/output.docx")
