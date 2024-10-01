import cv2
import easyocr

with open("usn_list.txt", 'r') as usns:
    usn_list = []
    for usn in usns:
        usn_list.append(str(usn))


# function for cropping
def image_crop(image_path):
    image = cv2.imread(image_path)
    # print(image.shape)
    cropped_img = image[21:57, 15:140]
    crop_path = "crop.png"
    cv2.imwrite(crop_path, cropped_img)
    return crop_path


#function for color change
def captcha_clr_change(image_path):
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    filename = "contchange.png"
    cv2.imwrite(filename, gray)
    return filename


#function for text conversion
def image_to_text(image_path):

    crop_path = image_crop(image_path)
    clrchange_path = captcha_clr_change(crop_path)
    
    reader = easyocr.Reader(['en'])
    result = reader.readtext(clrchange_path)

    for detection in result:
        text = detection[1]
        return text
    
#Function for Cropping the Result ScreenShot
def crop_result(result_path):

    image = cv2.imread(result_path)
    image = image[0:1017, 175:840]
    # result_path = "result\\{usn}.png".format(usn = str(usn_list[i]))
    cv2.imwrite(result_path, image)

# print(usn_list)
# crop_result("pdf\\test.png")
# print(image_to_text('captcha.png'))