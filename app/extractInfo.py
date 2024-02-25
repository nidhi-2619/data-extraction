import pytesseract
import pdf2image
from PIL import Image
PATH = r'C:\Users\Nidhi Nishad\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = PATH

def extract_text_from_image(imagePath: str) -> str | None:
    """Extract text data from the image."""
    image = Image.open(imagePath)
    text = pytesseract.image_to_string(image)
    return text

def convert_pdf_to_img(pdfPath: str) -> str:
    """Extract text data from the PDF."""
    images = pdf2image.convert_from_path(pdfPath, 500, poppler_path=r'C:\Program Files\poppler-24.02.0\Library\bin')
    filename = ""
    for i, image in enumerate(images):
        filename = pdfPath.replace('.pdf', f'.png')
        image.save(filename, "PNG")
    return filename


def check_file_type(filePath: str):
    """Check the file type of the given file."""
    if filePath.endswith('.pdf'):
        content = convert_pdf_to_img(filePath)
        content = extract_text_from_image(content)
    elif filePath.endswith(('.jpg', '.jpeg', '.png')):
        content = extract_text_from_image(filePath)
    else:
        raise ValueError("File type not supported")
    return content




