import cv2
import numpy as np 
#function to apply the filter
def apply_filter(image, filter_type):
    #copy the image-avoid modifying the original image
    filtered_image = image.copy()
    #filter types
    if filter_type=="red-tint":
        #remove green and blue channels
        filtered_image[:,:,1]=0 #green channel
        filtered_image[:,:,0]=0 #blue channel
    if filter_type=="green-tint":
        #remove blue and red
        filtered_image[:,:,2]=0 #red channel
        filtered_image[:,:,0]=0 #blue channel
    if filter_type=="blue-tint":
        #remove red and green
        filtered_image[:,:,2]=0 #red channel
        filtered_image[:,:,1]=0 #green channel
    #increase the intensity of any colors
    if filter_type=="increase red":
        filtered_image[:,:,2]=cv2.add(filtered_image[:,:,2],50)
    if filter_type=="decrease green":
        filtered_image[:,:,1]=cv2.subtract(filtered_image[:,:,1],50)
    return filtered_image
#main function #load the image
image_path="image.png"
img=cv2.imread(image_path)
#check if image was loaded successfully
if img is None:
    print("Error:Image not found")
else:
    #default filter
    filter_type="original"
    #instructions to the user
    print("Press the following keys to apply filters")
    print("R-Red Tint")
    print("G-Green Tint")
    print("B-Blue Tint")
    print("I-Increase Red intensity")
    print("D-Decrease Green intensity")
    print("Q-quit")
    while True:
        #apply the fiter on the selected image'
        filtered_image=apply_filter(img,filter_type)
        cv2.imshow("Filtered Image",filtered_image)
        #wait for user to click on a button
        key=cv2.waitKey(0)&0XFF
        if key ==ord('r'):
            filter_type="red-tint"
        if key ==ord('g'):
            filter_type="green-tint"
        if key ==ord('b'):
            filter_type="blue-tint"
        if key ==ord('i'):
            filter_type="increase red"
        if key ==ord('d'):
            filter_type="decrease green"
        if key ==ord('q'):
            print("Exiting....")
            break
cv2.destroyAllWindows()