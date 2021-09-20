def ocr(image):
  import pytesseract, os
  try: 
    os.system('tesseract');os.system('clear')
  except: 
    os.system('install-pkg tesseract-ocr')
  pytesseract.pytesseract.tesseract_cmd = "tesseract"
  os.environ["TESSDATA_PREFIX"]  = "/home/runner/.apt/usr/share/tesseract-ocr/4.00/tessdata/"
  import cv2
  import numpy as np
  image = cv2.imread(image)


  def get_grayscale(image):
      return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  def remove_noise(image):
      return cv2.medianBlur(image,5)
  def thresholding(image):
      return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
  def dilate(image):
      kernel = np.ones((5,5),np.uint8)
      return cv2.dilate(image, kernel, iterations = 1)
  def erode(image):
      kernel = np.ones((5,5),np.uint8)
      return cv2.erode(image, kernel, iterations = 1)
  def opening(image):
      kernel = np.ones((5,5),np.uint8)
      return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
  def canny(image):
      return cv2.Canny(image, 100, 200)
  def deskew(image):
      coords = np.column_stack(np.where(image > 0))
      angle = cv2.minAreaRect(coords)[-1]
      if angle < -45:
          angle = -(90 + angle)
      else:
          angle = -angle
      (h, w) = image.shape[:2]
      center = (w // 2, h // 2)
      M = cv2.getRotationMatrix2D(center, angle, 1.0)
      rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
      return rotated
  def match_template(image, template):
      return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 
  image = get_grayscale(image)
  #image = deskew(image)
  #image = thresholding(image)
  #image = remove_noise(image)
  #image = opening(image)
  #image = erode(image)
  #image = canny(image)
  #image = dilate(image)

  h, w = image.shape
  boxed_image = pytesseract.image_to_boxes(image)
  for b in boxed_image.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)


  cv2.imwrite('output.png',img)
  return pytesseract.image_to_string(image)