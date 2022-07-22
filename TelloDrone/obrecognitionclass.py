import cv2
from djitellopy import tello
import cvzone
from ObjectFollowing import drone, myFrame




class balldetect:
    def __init__(self):
        cap = cv2.VideoCapture(myFrame)
        cap.set(3, 640)
        cap.set(4, 480)

        classNames = []
        classFile = 'coco.names'
        with open(classFile, 'rt') as f:
            classNames = f.read().split('\n')
        #print(classNames)
        configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        weightsPath = 'frozen_inference_graph.pb'
        thres = 0.35
        nmsThres = 0.2
        net = cv2.dnn_DetectionModel(weightsPath, configPath)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        self.cap = cap
        self.classNames = classNames
        self.classFile = classFile
        self.configPath = configPath
        self.weightsPath = weightsPath
        self.thres = thres
        self.nmsThres = nmsThres
        self.net = net
    def close(self):
        cv2.DestroyWindow("Image")
    def balldetect(self):
        success, img = self.cap.read()
        classIds, confs, bbox = self.net.detect(img, confThreshold=self.thres, nmsThreshold=self.nmsThres)
        try:
            for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
                if classId == 37:
                    tf = True
                    print(tf)
                    return True
        except:
            pass
        cv2.imshow("Image", img)
        cv2.waitKey(1)




if __name__ == "__main__":
    while True:
        bd = balldetect()
        bd.balldetect()