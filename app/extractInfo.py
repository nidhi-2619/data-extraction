import pytesseract
import pdfplumber
from PIL import Image

def extract_text_from_image(imagePath: str) -> str:
    """Extract text data from the image."""
    image = Image.open(imagePath)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdfPath: str) -> str:
    """Extract text data from the PDF."""
    text = ""
    with pdfplumber.open(pdfPath) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def check_file_type(filePath: str):
    """Check the file type of the given file."""
    if filePath.endswith('.pdf'):
        data = extract_text_from_pdf(filePath)
    elif filePath.endswith(('.jpg', '.jpeg', '.png')):
        data = extract_text_from_image(filePath)
    else:
        raise ValueError("File type not supported")

    return data


def text_to_csv(data: str, csvPath: str):
    """Convert the extracted text to a CSV file."""
    pass



if __name__ == "__main__":
    # Test the functions
    pdfPath = "sample.pdf"
    imagePath = "sample.png"
    print(check_file_type(pdfPath))
    print(check_file_type(imagePath))
