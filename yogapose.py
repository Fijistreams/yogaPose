import cv2
import mediapipe as mp
import PoseModule as pm

def checkPose(pose):
    cap = cv2.VideoCapture('downwarddog.mp4')
    #cap = cv2.VideoCapture(0)

    detector = pm.poseDetector()
    if(pose == 'downwarddog'):

        while True:
            try:
                success, img = cap.read()
                img = cv2.resize(img, (1280,720))
                #img = cv2.imread('downDog.jpg')
                img = detector.findPose(img, False)
                lmlist = detector.findPosition(img, False)
            except Exception:
                exit(0)

            if(len(lmlist) != 0):
                hipangle = detector.findAngle(img, 12, 24, 26)
                armangle = detector.findAngle(img, 12, 14, 16)
                legangle = detector.findAngle(img, 24, 26, 28)

                if(100 > hipangle > 71 and 150 < armangle < 180 and 190 >= legangle >= 170):
                    #print('Correct!')
                    cv2.putText(img,"Correct",(70,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),3)
                else:
                    cv2.putText(img,"Incorrect",(70,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),3)
            cv2.imshow("image", img)
            cv2.waitKey(1)
    
    if(pose == 'lotus'):
         while True:
            try:
                success, img = cap.read()
                img = cv2.resize(img, (1280,720))
                #img = cv2.imread('downDog.jpg')
                img = detector.findPose(img, False)
                lmlist = detector.findPosition(img, False)
            except Exception:
                exit(0)

            if(len(lmlist) != 0):
                hipangle = detector.findAngle(img, 12, 24, 26)
                legs = detector.findAngle(img, 24, 26, 28)
                arms = detector.findAngle(img, 12, 14, 16)

                if(130 > hipangle >= 115 and 175 < legs < 181 and 200 >= arms >= 180):
                    #print('Correct!')
                    cv2.putText(img,"Correct",(70,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),3)
                else:
                    cv2.putText(img,"Incorrect",(70,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),3)
                    cv2.putText(img,"hips are" + str(hipangle),(70,90),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),3)
                    cv2.putText(img,"arms are" + str(arms),(70,140),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),3)
                    cv2.putText(img,"legs are " + str(legs),(70,200),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),3)

            cv2.imshow("image", img)
            cv2.waitKey(1)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

checkPose('downwarddog')