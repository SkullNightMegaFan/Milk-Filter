import cv2

f = open("cv2-information", "w")
bodyText = print(cv2.getBuildInformation())
bodyTextString = str(bodyText)
f.write(bodyTextString)
f.close()