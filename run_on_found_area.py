import cv2
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from google.colab.patches import cv2_imshow
import numpy as np
import scipy.signal as sps
from scipy.signal import argrelextrema
import pandas as pd

from utils.area_signal import get_area_variatinon
from utils.features import features

'''
path = 'G:/DRIVE_F/InternshipNorway/Project_6_SimonFish/Dataset/Sample dataset'
path_x = path + '/' + 'X_area.csv'
path_y = path + '/' + 'Y_area.csv'

df_x = pd.read_csv(path_x)
df_y = pd.read_csv(path_y)

X = np.array(df_x['0'])
Y = np.array(df_y['0'])
f1, f2, f3, f4, f5, f6 = features(X, Y, path, '5')
'''
videos_path = 'G:/DRIVE_F/InternshipNorway/Project_6_SimonFish/Dataset/Total dataset/embryonic heart videos/6.21.21'
video_list = os.listdir(videos_path)
print(video_list)
featureset = []
for id in video_list:
    if id != 'Features': 
        print('Video ========> ', id)
        path = videos_path + '/Features/' + 'Areas/' + id
        df_x = pd.read_csv(path + '/X_area_normalized.csv')
        df_y = pd.read_csv(path + '/Y_area_normalized.csv')
        X = np.array(df_x['0'])
        Y = np.array(df_y['0'])
        arr = features(X, Y, videos_path, id)
        featureset.append(arr)

df_features = pd.DataFrame(featureset)
df_features.to_csv(videos_path + '/Features' + '/Traditional Features' + '/' + '6.21.21.csv')
