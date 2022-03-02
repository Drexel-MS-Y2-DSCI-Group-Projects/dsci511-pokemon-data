from collections import Counter
from sklearn.cluster import KMeans
import cv2
import numpy as np
import requests

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
def get_hex_codes_for_img(url=None, path=None):
    if not url and not path:
        return []

    if url:
        image_title = url.split('/')[-1]
    else:
        image_title = path.split('/')[-1]

    extension = image_title.split('.')[1].casefold()
    
    if not extension in allowable_extensions:
        return []

    if url:
        img = requests.get(url, stream=True).content
    else:
        img = open(path, "rb").read()

    # Decode raw data to create a numpy array which cv2 understands
    arr = np.asarray(bytearray(img), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converts to RBG colors

    modified_image = prep_image(img) # preps the image, resizing and reshaping
    hex_colors = color_analysis(modified_image) # does the final colors analysis to get top 5 hex codes

    return hex_colors # return the list of hex colors
