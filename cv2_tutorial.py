import cv2
def main():
    impath="D:\shubham\shubham top secrate\shubham.jpg"
    
    img=cv2.imread(impath)#cv2.readimg(impath,0) will display grey scale img and 1 will display RBG image
    outpath="D:\django\shubham1.jpg"
    print(type(img))#dtype is nd array
    print(img.dtype)#unit 8 means its range is from 0-255 for gray scale 0-gray and 255-black
    print(img.shape)#resolution of the image 3 represent chanels
    print(img.ndim)# dimension of image only gray scale image have 2D
    print(img.size)#size of image
    
    

    #cv2.imshow("frame",img)
    #cv2.imwrite(outpath,img)#use to write the image at perticualr position
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
if __name__=="__main__":
    main()
