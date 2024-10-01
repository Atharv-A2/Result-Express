import pywhatkit
import time


def send_msg(rec, img, name, sgpa):
    try:

        #Sending the Message and their attached result to them using their Phone Number.
        pywhatkit.sendwhats_image("{receiver}".format(receiver = rec),"{img_path}".format(img_path = img), 
"Hey *{name}*, \nAnother Semester Down Buddy, Another Win in the Bag! \nCongrats on Surviving the College Shit and Coming Out Breathing!\n😎🤩🌟🙌 \n\nHere is a Quick Glance of your *Exceptional Performance*(My Opinion)😂😂!! \nSGPA - *{sgpa}* \n\nThis is an Automated Message, \nPlease *feel free* to Reply Back(It Replies Faster than the Human User). \nThanks!!🙏".format(name = name, sgpa = sgpa), 27, True, 4)
            
        print("Sent Successfully!")
    except Exception as e:
        print("Unexpected Error - ", e)

# name_list = open("name_list.txt", 'r').readlines()
# print(time.ctime(time.time()))
# for i in range(2):
#     send_msg("+917667700645", "pdf/test.png", name_list[i])
# print(time.ctime(time.time()))