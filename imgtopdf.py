from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation
from pathlib import Path

def convert(u_input: str):
    filepath = Path('./' + u_input)
    image = Image.open(filepath)
    pdfpath = str(filepath) + '_pdf.pdf'
    image.save(pdfpath, "PDF", resolution=100.0, save_all=True)
    print(f'File saved as {pdfpath}')

def main():
    root = Path('.')
    print('Files in folder:')
    for file in root.glob('*'):
        print(str(file))
    userinput = input('Please type the name of the image to convert to pdf: ')
    convert(userinput)

if __name__ == "__main__":
    main()