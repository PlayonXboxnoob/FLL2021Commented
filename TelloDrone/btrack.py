import cvzone
from cvzone.ColorModule import ColorFinder
import cv2








cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
success, img = cap.read()
h, w, _ = img.shape
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 103, 'smin': 80, 'vmin': 100, 'hmax': 128, 'smax': 255, 'vmax': 220}
global data







def GetPos():
    while True:
        global data
        success, img = cap.read()
        imgColor, mask = myColorFinder.update(img, hsvVals)
        imgContour, contours = cvzone.findContours(img, mask)


        if contours:
            data = contours[0]['center'][0], \
                    h - contours[0]['center'][1], \
                    int(contours[0]['area'])
            print(data)

        # imgStack = cvzone.stackImages([img, imgColor, mask, imgContour], 2, 0.5)
         # cv2.imshow("Image", imgStack)
        imgContour = cv2.resize(imgContour, (0, 0), None, 0.5, 0.5)
        cv2.imshow("ImageContour", imgContour)
        return data

