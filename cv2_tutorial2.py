import cv2
import numpy as np
def main():
    impath="D:\shubham\shubham top secrate\shubham.jpg"
    
    img=np.zeros((512,512,3),np.uint8)
    cv2.line(img,(0,99),(99,0),(255,0,0),2)#(x-axis,y-axis,color,thickness)
    cv2.rectangle(img,(40,60),(80,70),(0,255,0),2)
    cv2.circle(img,(60,60),10,(0,0,255),-1)#thickness -1 will fill entire circle
    text1="shubham"
    cv2.putText(img,text1,(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0))
    cv2.imshow("frame",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()
