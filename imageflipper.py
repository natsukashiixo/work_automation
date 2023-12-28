from pathlib import Path

from PIL import Image, ImageOps
import natsort

subdir = Path('./imagestomerge')

def iter_files(_dir):
    _process = [file for file in _dir.glob('*.jpg')]
    natsort.os_sorted(_process)
    for i, imgfile in enumerate(_process):
        if i % 2 == 1:
            pil_flip(imgfile)

def pil_flip(file_object):
    pil_image = Image.open(file_object)
    flipped = ImageOps.flip(pil_image)
    flip_mir = ImageOps.mirror(flipped)
    new_filename = file_object.stem + '_flipped.jpg'
    new_filepath = file_object.parent / new_filename
    flip_mir.save(new_filepath, format='JPEG')
    print(f'image flipped and saved as {new_filepath}')

if __name__ == '__main__':
    iter_files(subdir)