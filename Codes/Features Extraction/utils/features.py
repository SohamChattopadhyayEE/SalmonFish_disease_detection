import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from google.colab.patches import cv2_imshow
import numpy as np
import scipy.signal as sps
from scipy.signal import argrelextrema

from Spectrograms import Spectrograms


def local_minimas_maximas(X, Y):
  b, a = sps.butter(1, 0.02529)
  # Filter
  filtered = sps.filtfilt(b, a, Y)
  # for local maxima
  arr_maxima = argrelextrema(filtered, np.greater)
  print("No. of maximas: ", len(arr_maxima[0]))
  arr_minima = argrelextrema(filtered, np.less)
  print("No. of minimas: ", len(arr_minima[0]))
  plt.plot(X, filtered, color='blue', linewidth=1.5)
  #plt.show()
  return arr_maxima, arr_minima, filtered



def features(X, Y, out_path, image_name):
  arr_maxima, arr_minima, filtered = local_minimas_maximas(X, Y)
  print('Saving the spectrograms ===================>')
  Spectrograms(out_path, X, filtered, image_name)
  first_CPhase = (arr_maxima[0][1] - arr_minima[0][0])*10
  second_CPhase = (arr_maxima[0][2] - arr_minima[0][1])*10
  time_till_second_CPhase = (arr_minima[0][2] - 0)*10
  time_1st_2nd_CPhase = (arr_maxima[0][2] - arr_maxima[0][1])*10
  pulse = len(arr_maxima[0])

  total_CPhase = 0
  for i in range(1, pulse-1):
    total_CPhase += (arr_maxima[0][i] -  arr_minima[0][i-1])*10
  average_CPhase = total_CPhase/pulse

  #print(first_CPhase, second_CPhase, time_till_second_CPhase, time_1st_2nd_CPhase, pulse, average_CPhase)
  #arr = list(first_CPhase, second_CPhase, time_till_second_CPhase, time_1st_2nd_CPhase, pulse, average_CPhase)
  return [first_CPhase, second_CPhase, time_till_second_CPhase, time_1st_2nd_CPhase, pulse*2, average_CPhase]