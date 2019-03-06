import cv2
""""For caturing images
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
cv2.imshow("frame",img)
cv2.waitKey(0)
cap.release()
 cv2.destroyAllWindows()
 """
#for live video
cap=cv2.VideoCapture(0)
print("width"+str(cap.get(3)))
print("height"+str(cap.get(4)))
cap.set(3,400)
cap.set(4,400)
print("width"+str(cap.get(3)))
print("height"+str(cap.get(4)))
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
while ret:
    ret,frame=cap.read()
    output=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",output)
    cv2.imshow("frame1",frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
