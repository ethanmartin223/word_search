def ocr(image):
  #One time install-
  #import os; os.system('wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata')
  try:
    import os, pytesseract
    from PIL import Image,ImageFilter
    pytesseract.pytesseract.tesseract_cmd = "tesseract"
    os.environ["TESSDATA_PREFIX"]  = "/home/runner/.apt/usr/share/tesseract-ocr/4.00/tessdata/"
    image = Image.open(image)
    return pytesseract.image_to_string(image)
  except:
    os.system('install-pkg tesseract-ocr')
    exit('Package Installed Re-run the program')

data = ocr('puzzle.png')
print(data)