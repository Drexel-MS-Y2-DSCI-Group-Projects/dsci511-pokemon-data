from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import requests
import os

allowable_extensions = ['jpg','png']

# function to get the hex color from RGB color
def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color

# function to prepare the image for color analysis, doing resizing and modifying its shape
def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation = cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
    return modified_img

# function to do the color analysis of the image
def color_analysis(img):
    clf = KMeans(n_clusters = 5)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    return hex_colors

# function to pull an image from URL, and analyze it for its hex colors
def get_hex_codes_for_img(url):
    image_title = url.split('/')[-1]
    extension = image_title.split('.')[1].casefold()
    
    if (extension in allowable_extensions):
        img = Image.open(requests.get(url, stream=True).raw)
        img.save(image_title) # saves image from URL

        image = cv2.imread(image_title) # reads in the image from saved location
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # converts to RBG colors

        modified_image = prep_image(image) # preps the image, resizing and reshaping
        hex_colors = color_analysis(modified_image) # does the final colors analysis to get top 5 hex codes

        os.remove(image_title) # delete the image from disk

        return hex_colors # return the list of hex colors
    else:
        return []