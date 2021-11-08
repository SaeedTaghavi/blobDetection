import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import skimage
from skimage.io import imread, imshow
from skimage.color import rgb2gray, rgb2hsv
from skimage.measure import label, regionprops, regionprops_table
from skimage.filters import threshold_otsu
from scipy.ndimage import median_filter
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from tqdm import tqdm
def func1():
    #load image
    img = cv2.imread('./frames/frame0.jpg')
    plt.imshow(img,cmap = 'gray')
    plt.show()

    #apply median blur, 15 means it's smoothing image 15x15 pixels
    blur = cv2.medianBlur(img,15)
    plt.imshow(blur)
    plt.show()
    #convert to hsv
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    #color definition
    red_lower = np.array([160,210,230])
    red_upper = np.array([180,255,255])

    #red color mask (sort of thresholding, actually segmentation)
    mask = cv2.inRange(hsv, red_lower, red_upper)

    connectivity = 4  
    # Perform the operation
    output = cv2.connectedComponentsWithStats(mask, connectivity, cv2.CV_32S)
    # Get the results

    num_labels = output[0]-1

    centroids = output[3][1:]
    #print results
    print ('number of dots, should be 4:',num_labels )
    print ('array of dot center coordinates:',centroids)
def threshold_checker(image):
    thresholds =  np.arange(0.1,1.1,0.1)
    tree_gray = rgb2gray(image)
    fig, ax = plt.subplots(2, 5, figsize=(17, 10))
    for n, ax in enumerate(ax.flatten()):
        ax.set_title(f'Threshold  : {round(thresholds[n],2)}',      
                       fontsize = 16)
        threshold_tree = tree_gray < thresholds[n]
        ax.imshow(threshold_tree);
        ax.axis('off')
    fig.tight_layout()

def func2():


    tree = imread('./frames/frame0.jpg')
    # tree = cv2.medianBlur(tree,15)
    tree_gray = rgb2gray(tree)
    # plt.imshow(tree_gray,cmap='gray')
    # plt.imshow(tree_gray,cmap='gray')
    otsu_thresh = threshold_otsu(tree_gray)
    tree_binary = tree_gray < otsu_thresh
    # plt.imshow(tree_binary, cmap = 'gray')
    # threshold_checker(tree)
    
    tree_hsv = rgb2hsv(tree[:,:,:])
    # plt.figure(num=None, figsize=(8, 6), dpi=80)
    # plt.imshow(tree_hsv[:,:,0], cmap='hsv')
    # plt.colorbar()
    # plt.show()
    lower_mask0 = tree_hsv [:,:,0] > .000
    # upper_mask0 = tree_hsv [:,:,0] > 10.00
    lower_mask1 = tree_hsv [:,:,1] > 0.60
    upper_mask1 = tree_hsv [:,:,1] <= 9.00
    lower_mask2 = tree_hsv [:,:,2] > 0.40
    upper_mask2 = tree_hsv [:,:,2] <= 7.00
    mask = lower_mask0* upper_mask1*lower_mask1*upper_mask2*lower_mask2
    red = tree[:,:,0]*mask
    green = tree[:,:,1]*mask
    blue = tree[:,:,2]*mask
    tree_mask = np.dstack((red,green,blue))
    # plt.figure(num=None, figsize=(8, 6), dpi=80)
    # imshow(red,cmap='Reds')
    # plt.show()
    # tree_hsv = rgb2hsv(tree[:,:,:])
    # plt.figure(num=None, figsize=(8, 6), dpi=80)
    # plt.imshow(tree_hsv[:,:,2], cmap='gray')
    # plt.colorbar();
    # plt.show()
    # lower_mask = tree_hsv [:,:,1] > 0.70
    # upper_mask = tree_hsv [:,:,1] <= 9.00
    # value_mask = tree_hsv [:,:,2] < .90
    # mask = upper_mask*lower_mask#*value_mask
    # red = tree[:,:,0] * mask
    # green = tree[:,:,1] * mask
    # # blue = tree[:,:,2] * mask
    # tree_mask = np.dstack((red, green, blue))
    # # plt.figure(num=None, figsize=(8, 6), dpi=80)
    # # imshow(tree_mask);
    # # plt.show()

    # lower_mask = tree_hsv [:,:,1] > 0.650
    # upper_mask = tree_hsv [:,:,1] <= 1.00
    # # value_mask = tree_hsv [:,:,2] < .90
    # mask = median_filter(upper_mask*lower_mask, 10)
    # red = tree[:,:,0] * mask
    # green = tree[:,:,1] * mask
    # blue = tree[:,:,2] * mask
    # tree_mask = np.dstack((red, green, blue))
    # plt.figure(num=None, figsize=(8, 6), dpi=80)
    # imshow(tree_mask);
    # plt.show()
    tree_blobs = label(rgb2gray(tree_mask) > 0)
    # imshow(tree_blobs, cmap = 'tab10');
    # plt.show()
    properties =['area','bbox','convex_area','bbox_area',
             'major_axis_length', 'minor_axis_length',
             'eccentricity']
    df = pd.DataFrame(regionprops_table(tree_blobs, properties = properties))
    blob_coordinates = [(row['bbox-0'],row['bbox-1'],
                     row['bbox-2'],row['bbox-3'] )for 
                    index, row in df.iterrows()]
    fig, ax = plt.subplots(1,1, figsize=(8, 6), dpi = 80)
    for blob in tqdm(blob_coordinates):
        width = blob[3] - blob[1]
        height = blob[2] - blob[0]
        patch = Rectangle((blob[1],blob[0]), width, height,linewidth=3, edgecolor='blue', facecolor='none')
        ax.add_patch(patch)
    ax.imshow(tree)
    ax.set_axis_off()
    plt.show()

func2()