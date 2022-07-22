import cvzone
from cvzone.ColorModule import ColorFinder
import cv2

from ObjectFollowing import drone, myFrame


class balltracking():


    def __init__(self):
        cap = cv2.VideoCapture(myFrame)
        cap.set(3, 1280)
        cap.set(4, 720)
        success, img = cap.read()
        h, w, _ = img.shape
        myColorFinder = ColorFinder(False)
        hsvVals = {'hmin': 103, 'smin': 80, 'vmin': 50, 'hmax': 128, 'smax': 255, 'vmax': 220}
        self.cap = cap
        self.h = h
        self.w = w
        self.myColorFinder=myColorFinder
        self.hsvVals = hsvVals

    def close(self):
        cv2.destroyWindow("ImageContour")
        cv2.quit
        cvzone.quit



    def GetPos(self):
        success, img = self.cap.read()
        imgColor, mask = self.myColorFinder.update(img, self.hsvVals)
        imgContour, contours = cvzone.findContours(img, mask)
        data = []

        if contours:
            data = [contours[0]['center'][0], \
                   self.h - contours[0]['center'][1], \
                   int(contours[0]['area'])]
            print(data)

        # imgStack = cvzone.stackImages([img, imgColor, mask, imgContour], 2, 0.5)
        # cv2.imshow("Image", imgStack)
        imgContour = cv2.resize(imgContour, (0, 0), None, 0.5, 0.5)
        cv2.imshow("ImageContour", imgContour)


        return data





if __name__ == "__main__":
    while True:
        ball = balltracking()
        pos = ball.GetPos()





