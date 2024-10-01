import time, os

# with open("usn_list.txt", "r") as usns:
#     usn_list = []
#     for usn in usns:
#         usn_list.append(str(usn))
#         # time.sleep(1)


# usn_list = open("usn_list.txt", 'r')
# usn_list = usn_list.readlines()
# print(type(usn_list[0]))

receiver_list = open("receiver_list.txt", 'r').readlines()

for x in range(len(receiver_list)):
    
    # print(result_imgs)
    print(receiver_list[0].rstrip('\n'))
print(x)