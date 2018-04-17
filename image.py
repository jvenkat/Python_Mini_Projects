import cv2

img=cv2.imread("/sample-images",1)
img=cv2.resize(img,(1000,500))
cv2.imshow("Galaxy",img)
cv2.imwrite("Galaxy_.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
