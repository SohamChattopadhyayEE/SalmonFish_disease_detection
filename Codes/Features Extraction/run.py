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

videos_path = 'G:/DRIVE_F/InternshipNorway/Project_6_SimonFish/Dataset/Total dataset/embryonic heart videos/6.21.21'
video_list = os.listdir(videos_path)
print(video_list)
featureset = []
for id in video_list:
    if id != 'Features': 
        print('Video ========> ', id)
        video_path = videos_path + '/' + id
        print('Video path =======> ', video_path)
        out_area_path = videos_path + '/' + 'Features/' + 'Areas/' + id
        if not os.path.exists(out_area_path):
            os.mkdir(out_area_path)
        X, Y = get_area_variatinon(video_path, out_area_path)
        #f1, f2, f3, f4, f5, f6 = features(X, Y, videos_path, id)
        arr = features(X, Y, videos_path, id)
        #arr = {f1, f2, f3, f4, f5, f6}
        featureset.append(arr)

df_features = pd.DataFrame(featureset)
df_features.to_csv(videos_path + '/Features' + '/Traditional Features' + '/' + '6.21.21.csv')
