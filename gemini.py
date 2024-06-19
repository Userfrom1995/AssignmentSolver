import os
from docx import Document

import google.generativeai as genai

genai.configure(api_key="AIzaSyDFK4LtXHyeWqWC6lujHiznEg9cUmdHfJo")
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(
    "Assignment Programs write in c++:\n"
    "1. Programs for Newton-Gregory forward and backwards, Lagrange, and Newton's divided difference interpolation.\n\n"
    "2. Programs for Simpson's three-eight rule, Bool's and Weddle's rules, Trapezoidal, and Simpson's one-third rule.\n\n"
    "3. Programs for Bisection, Regula false position, and Newton Raphson method, Fitting a second-degree parabola and polynomial fitting.\n\n"
    "4. Programs for Gauss Elimination, Gauss-Jordan, and Gauss-Seidal methods, Magic square, and Marks Sheet programs.\n\n"
    "5. Programs on Modified Euler's method, RK method for system and second-order differential Equation, and Milney's method, a program on the use of functions.\n\n"
    "6. Programs on Sine And cosine series and function subprogram for matrices multiplication."
)

# Save the response output to a Word file
def save_to_word(text, output_file_path):
    # Create a new Word document
    doc = Document()

    # Add a paragraph with the text to the document
    doc.add_paragraph(text)

    # Save the Word document
    doc.save(output_file_path)

# Specify the output file path
output_file_path = "output.docx"

# Save the response output to the Word file
save_to_word(response.text, output_file_path)

print(f"Response output saved to '{output_file_path}'")