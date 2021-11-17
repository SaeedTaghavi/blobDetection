import cv2
import  math
import numpy as np
import cv2


# def find_the_boggest_contour(contour):

# read the image
fullPath='./frames/frame0.jpg'
image = cv2.imread(fullPath)

# B, G, R channel splitting
blue, green, red = cv2.split(image)
# print(np.shape(red))
# cv2.imshow("red",red)
# cv2.imshow("blue",blue)
# cv2.imshow("green",green)
# cv2.waitKey(0)

# detect contours using blue channel and without thresholding
contours1, hierarchy1 = cv2.findContours(image=blue, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
# draw contours on the original image
image_contour_blue = image.copy()
cv2.drawContours(image=image_contour_blue, contours=contours1, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# see the results
# cv2.imshow('Contour detection using blue channels only', image_contour_blue)
# cv2.waitKey(0)
# cv2.imwrite('blue_channel.jpg', image_contour_blue)
# cv2.destroyAllWindows()

# detect contours using green channel and without thresholding
contours2, hierarchy2 = cv2.findContours(image=green, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
# draw contours on the original image
image_contour_green = image.copy()
cv2.drawContours(image=image_contour_green, contours=contours2, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# see the results
# cv2.imshow('Contour detection using green channels only', image_contour_green)
# cv2.waitKey(0)
# cv2.imwrite('green_channel.jpg', image_contour_green)
# cv2.destroyAllWindows()

# detect contours using red channel and without thresholding
# ret, thresh1 = cv2.threshold(blue, 50, 255, cv2.THRESH_BINARY_INV)
ret, thresh = cv2.threshold(blue, 50, 255, cv2.THRESH_BINARY_INV)
ret, threshr = cv2.threshold(red, 50, 255, cv2.THRESH_BINARY)
threshm = thresh*threshr
# cv2.imshow("r",threshr)
# cv2.imshow("b",thresh)
# cv2.imshow("r*b",threshm)
# cv2.waitKey(0)
# ret, thresh = cv2.threshold(red, 110, 120, cv2.THRESH_BINARY)
contours3, hierarchy3 = cv2.findContours(image=threshm, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
print("num contours: ",len(contours3))
c = max(contours3, key = cv2.contourArea)
area = cv2.contourArea(c)
perimeter = cv2.arcLength(c,True)
M = cv2.moments(c)
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
else:
    cX, cY = 0, 0



# print(contours3)
# draw contours on the original image
image_contour_red = image.copy()
cv2.drawContours(image=image_contour_red, contours=c, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# see the results
cv2.circle(image_contour_red, (cX, cY), 5, (255, 255, 255), -1)   #center of mass contour
# x,y,w,h = cv2.boundingRect(c)
# cv2.rectangle(image_contour_red,(x,y),(x+w,y+h),(0,255,0),2)
# rect = cv2.minAreaRect(c)
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# cv2.drawContours(image_contour_red,[box],0,(0,0,255),2)
# ellipse = cv2.fitEllipse(c)
# cv2.ellipse(image_contour_red,ellipse,(0,255,0),2)
cv2.imshow(fullPath, image_contour_red)
cv2.waitKey(0)
cv2.imwrite('red_channel.jpg', image_contour_red)
cv2.destroyAllWindows()













# im = cv2.imread('./frames/frame0.jpg')
# imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# im_gauss = cv2.GaussianBlur(imgray, (5, 5), 0)
# ret, thresh = cv2.threshold(im_gauss, 127, 255, 0)
# # get contours
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# contours_area = []
# # calculate area and filter into new array
# for con in contours:
#     area = cv2.contourArea(con)
#     if 1000 < area < 10000:
#         contours_area.append(con)

# contours_cirles = []

# # check if contour is of circular shape
# for con in contours_area:
#     perimeter = cv2.arcLength(con, True)
#     area = cv2.contourArea(con)
#     if perimeter == 0:
#         break
#     circularity = 4*math.pi*(area/(perimeter*perimeter))
#     print (circularity)
#     if 0.7 < circularity < 1.2:
#         contours_cirles.append(con)



# image = cv2.imread('./frames/frame0.jpg')
# img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # apply binary thresholding
# ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# # visualize the binary image
# cv2.imshow('Binary image', thresh)
# cv2.waitKey(0)
# cv2.imwrite('image_thres1.jpg', thresh)
# cv2.destroyAllWindows()
# # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
# contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
# # draw contours on the original image
# image_copy = image.copy()
# cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
               
# # see the results
# cv2.imshow('None approximation', image_copy)
# cv2.waitKey(0)
# cv2.imwrite('contours_none_image1.jpg', image_copy)
# cv2.destroyAllWindows()