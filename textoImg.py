import pytesseract
import cv2
import os

# Set the TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/'
# Set the path to the Tesseract executable for Linux
tesseract_cmd = "/usr/bin/tesseract"

for i in range(33):


    for i in range(33):
        image_path = f'teste_{i}.png'
        imagem = cv2.imread(image_path)

        if imagem is not None:
            # Perform preprocessing (e.g., resizing, grayscale conversion)
            # Example: imagem = cv2.resize(imagem, (width, height))

            texto = pytesseract.image_to_string(imagem, config=tesseract_cmd)
            print(f"Text from image {i}:\n{texto}")
            imagem.save(f'texto_{i}.txt', 'TXT')
        else:
            print(f"Failed to load image: {image_path}")