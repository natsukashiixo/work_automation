import pdf2image
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pathlib import Path
from PIL import Image

popplerpath = r'C:\Users\jera500\Documents\poppler\Library\bin'

def convert(u_input):
    filepath = Path('./' + u_input)
    image = pdf2image.convert_from_path(filepath, poppler_path=popplerpath, output_folder='.', fmt="jpeg")

def main():
    root = Path('.')
    print('Files in folder:')
    for file in root.glob('*'):
        print(str(file))
    userinput = input('Please type the name of the pdf to convert to jpeg: ')
    convert(userinput)

if __name__ == "__main__":
    main()
    