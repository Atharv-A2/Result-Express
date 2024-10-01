# import pytesseract
import cv2
from PIL import Image
import easyocr, numpy as np
from rembg import remove

# pytesseract.pytesseract.tesseract_cmd = str('E:\\Programs\\Tesseract-OCR\\tesseract.exe')

def captcha_to_string(image_path):
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    filename = "contchange1.png"
    cv2.imwrite(filename, gray)
    # captcha_text = pytesseract.image_to_string(Image.open('contchange.png'))
    # print(captcha_text)
    # cv2.imshow("fff", image)
    # cv2.waitKey(0)
    # return captcha_text


def image_to_text(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    for detection in result:
        text = detection[1]
        return text

def bgr_remove(image_path):
    image = Image.open(image_path)
    clr_img = remove(image)
    clr_img.save('newimage.png')


def bgremove2(image_path):
    # First Convert to Grayscale
    myimage = cv2.imread(image_path)
    myimage_grey = cv2.cvtColor(myimage, cv2.COLOR_BGR2GRAY)
 
    ret,baseline = cv2.threshold(myimage_grey,127,255,cv2.THRESH_TRUNC)
 
    ret,background = cv2.threshold(baseline,126,255,cv2.THRESH_BINARY)
 
    ret,foreground = cv2.threshold(baseline,126,255,cv2.THRESH_BINARY_INV)
 
    foreground = cv2.bitwise_and(myimage,myimage, mask=foreground)  # Update foreground with bitwise_and to extract real foreground
 
    # Convert black and white back into 3 channel greyscale
    background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)
 
    # Combine the background and foreground to obtain our final image
    finalimage = background+foreground
    cv2.imwrite('bgr.png', finalimage)
    # return finalimage


#function for cropping
# captcha_to_string("captcha.png")

bgremove2('contchange.png')
print(image_to_text('bgr.png'))
# bgr_remove('contchange1.png')
print("Done")
