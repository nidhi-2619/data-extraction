# Data Extraction

This is a web application made using Django and Python.
The user upload a file in PDF or Image format and the application will extract the text from the file  
and create a downloadable csv file with the extracted text.

The libraries used for the text extraction are:
 - [pdf2image](https://pypi.org/project/pdf2image/)
 - [pytesseract](https://pypi.org/project/pytesseract/)
 - [PIL](https://pypi.org/project/Pillow/)

Before running the application, make sure to have installed the following:
 - [Tesseract](https://github.com/tesseract-ocr/tesseract)
 - [Poppler](https://poppler.freedesktop.org/)
 - [Python](https://www.python.org/)
 - [Poetry](https://python-poetry.org/)
 - [Node.js](https://nodejs.org/en/)



## Installation

#### Clone the repository to your local machine
```bash
git clone https://github.com/nidhi-2619/data-extraction.git
```
#### Install the dependencies using poetry and npm

```bash
poetry install
```

```nodemon
npm install
```

## Run TailwindCSS

```nodemon
npm run dev
```

## Run Server
    
```python
python manage.py runserver
```


