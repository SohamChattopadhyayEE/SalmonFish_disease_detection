# Cardiac disease detection in Salmon fishes
Cardiac diseases in salmon significantly affect Norway’s economy. An estimated loss of more than € 25 million was attributed to cardiomyopathy syndrome in salmon in 2007 and the numbers are increasing steadily. Cardiomyopathy syndrome  traditionally  manifests  itself  in salmon  12  to  18  months  after  transfer  to  seawater,  and affected  fish  frequently  die  without  any  prior  clinical signs of the disease. Scientists are working on finding ways of studying the behaviour of infected salmon heart in contrast to healthy one. This shall potentially help in detecting the disease in salmon fishes as early possible such that the economic loss can be addressed up to a certain extent. 

The objective of this paper is to classify salmon hearts are infected on otherwise by using videos of embryonic heart to identify various physical parameters that allow classification. In this present study, controlled eggs of salmon fishes are embryonated and their embryonic hearts are put under observation. Furthermore different videos at different time frames are recorded which provides valuable information about the changes of behaviours of embryonic hearts. Thereafter, based on certain attributes extracted from this data, various predictive artificial intelligence models are used for the classification purpose. 

## Experiment Details
- #### Dataset 
    The dataset is consisted of several `.avi` videos of 10 embryonic Salmon hearts. Among which 5 are infected and 5 are healthy. Videos are recorded at three different time   frames, that is on Day 0, Day 7 and Day 21. However, most of the embryonic hearts did not survive till Day 21. This task focuses on detecting diseased hearts as early as possible. However at Day 0, since the disease just start effecting the heart, no significant abnormality or distortions in tissues are found between the healthy and ill hearts. Therefore, the aim of finding and seperating ill hearts gets narrowed down to the data obtained on Day 7 only. 
- #### Features 
    - First from the video data a signal depicting the variation of size of the heart is generated. 
    - From the signal following `8` features are extracted-
      - pulse rate (PR)
      - time of first contraction phase(CP1)
      - time of second contraction phase (CP2)
      - time till sec-ond contraction phase (tCP)
      - time between first and secondcontraction phase (CP21)
      - average contraction phase (ACP)
      - standard deviation of the contraction phase (SDCP)
      - spectrogram
      
