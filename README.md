# Cardiac Disease Detection in Salmon Fishes
Cardiac diseases in salmon significantly affect Norway’s economy. An estimated loss of more than € 25 million was attributed to cardiomyopathy syndrome in salmon in 2007 and the numbers are increasing steadily. Cardiomyopathy syndrome  traditionally  manifests  itself  in salmon  12  to  18  months  after  transfer  to  seawater,  and affected  fish  frequently  die  without  any  prior  clinical signs of the disease. Scientists are working on finding ways of studying the behaviour of infected salmon heart in contrast to healthy one. This shall potentially help in detecting the disease in salmon fishes as early possible such that the economic loss can be addressed up to a certain extent. 

The objective of this paper is to classify salmon hearts are infected on otherwise by using videos of embryonic heart to identify various physical parameters that allow classification. In this present study, controlled eggs of salmon fishes are embryonated and their embryonic hearts are put under observation. Furthermore different videos at different time frames are recorded which provides valuable information about the changes of behaviours of embryonic hearts. Thereafter, based on certain attributes extracted from this data, various predictive artificial intelligence models are used for the classification purpose. 

## Experiment details
- #### Dataset 
    The dataset is consisted of several `.avi` videos of 10 embryonic Salmon hearts. Among which 5 are infected and 5 are healthy. Videos are recorded at three different time   frames, that is on Day 0, Day 7 and Day 21. However, most of the embryonic hearts did not survive till Day 21. This task focuses on detecting diseased hearts as early as possible. However at Day 0, since the disease just start effecting the heart, no such discriminatory abnormality or distortions in tissues are found between the healthy and ill hearts. Therefore, the aim of finding and seperating ill hearts gets narrowed down to the data obtained on Day 7 only. The Day 7 dataset can be downloaded from [here](https://drive.google.com/drive/folders/1T2C58kKQvSJLvvfWZYVaozHHQ1bwH7-L?usp=sharing "Day 7 dataset").
- #### Features 
    - First from the video data a signal depicting the variation of size of the heart is generated. The flowdiagram of the signal generation process is illustrated in the following figure. ![Signal generation](https://github.com/SohamChattopadhyayEE/SalmonFish_disease_detection/blob/main/Figures/Signal_generation.JPG)
    - Once the signal is obtained, following `8` attributes can also be obtained from that signal-
      - pulse rate (PR)
      - time of first contraction phase(CP1)
      - time of second contraction phase (CP2)
      - time till sec-ond contraction phase (tCP)
      - time between first and secondcontraction phase (CP21)
      - average contraction phase (ACP)
      - standard deviation of the contraction phase (SDCP)
      - spectrogram
    - Spectrograms are extracted from three different filtration levels of the original signal. 
    - The signal generation from the video data and attributes extraction from the signal can be done by simply running the code [`run.py`](https://github.com/SohamChattopadhyayEE/SalmonFish_disease_detection/blob/main/Codes/Features%20Extraction/run.py), where only the path of the directory containing the videos should be given as input. 
- #### Classification 
    - For classification, 4 differents algorithms are chosen. Three among them are classical machine learning classifiers, such as SVM, KNN and MLP, and one is a shalow deep learning model called [LightOCT](https://www.osapublishing.org/boe/fulltext.cfm?uri=boe-11-9-5017&id=434402 "Link to the paper of LightOCT"). Among the aforementioned 8 features, first 7 are used for the machine learning based models and the last one, that is the spectrogram is used for the LightOCT. 

## Dependencies and packages
The entire code is in Python language. Therefore Python is the primary necessity to run the project. Following are the Python packages used in this project and should be installed in the system to run the codes. 
- `sklearn`
- `matplotlib`
- `numpy`
- `pandas`
- `scipy`
- `pytorch`
- `OpenCV`
- `os`

These packages can be installed in the local system by the command `pip install --package`. 
