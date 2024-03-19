import cv2
from cvzone import HandTrackingModule

#Capture video from default camera
cap=cv2.VideoCapture(0)

# Set the resolution (for 1280x720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector=HandTrackingModule.HandDetector()

while True:
     sucess,img=cap.read()
     
     detector.findHands(img)
     #for displaying the image
     cv2.imshow("Image",img)
    
     #For closing the live camera feed
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     
cap.release()
cv2.destroyAllWindows()