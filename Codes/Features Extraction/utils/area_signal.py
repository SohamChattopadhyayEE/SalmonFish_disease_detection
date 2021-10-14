import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from google.colab.patches import cv2_imshow
import numpy as np
import scipy.signal as sps
from scipy.signal import argrelextrema


def get_area_variatinon(video_path, out_path):

  cap = cv2.VideoCapture(video_path)

  no_of_frames = int(cap.get(7))
  print(no_of_frames)

  def get_contours(img, img_contour):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    res = 0
    for cnt in contours:
      area = cv2.contourArea(cnt)

      if area>3000:
        cv2.drawContours(img_contour, cnt, -1, (255, 0, 255), 2)
        res = area
    return res 

  X = []
  Y = []
  max_area = 0
  for i in range(no_of_frames):
    ret, frame = cap.read()
    #Contrast normalization
    cv2.normalize(frame, frame, 0, 255, cv2.NORM_MINMAX)

    # Resizing 
    img = cv2.resize(frame, (200, 200), interpolation = cv2.INTER_AREA)
    img_contour = img.copy()

    # Getting the canny image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (13,13), 0)
    edges = cv2.Canny(image=img_blur, threshold1=30, threshold2=30)

    # Dilation for noise removal
    kernel = np.ones((5, 5))
    img_dil = cv2.dilate(edges, kernel, iterations = 1)

    # Contour detection and finding the area
    area = get_contours(img_dil, img_contour)
    max_area = max(area, max_area)
    X.append(i)
    if area == 0 : 
      area = max_area
    Y.append(area)
    print("Frame no.: {}  / Total frame {}    Area: {}".format(i+1, no_of_frames, area))
    
    '''
    # Image show
    cv2_imshow(img)
    cv2_imshow(edges)
    cv2_imshow(img_dil)
    print('Area: ', area)
    cv2_imshow(img_contour)
    '''
  cap.release()
  df_x = pd.DataFrame(X)
  df_y = pd.DataFrame(Y)

  df_x.to_csv(out_path + '/' + 'X_area_normalized.csv')
  df_y.to_csv(out_path + '/' + 'Y_area_normalized.csv')

  return X, Y