import numpy as np
import pandas as pd

from classifiers import cross_folds_results
import warnings
warnings.filterwarnings("ignore")

# Give the paths of feature and label .csv files
features_path = 'G:/DRIVE_F/InternshipNorway/Project_6_SimonFish/Dataset/Total dataset/embryonic heart videos/6.21.21/Features/Traditional Features/6.21.21.csv'
lables_path = 'G:/DRIVE_F/InternshipNorway/Project_6_SimonFish/Dataset/Total dataset/embryonic heart videos/6.21.21/Features/Traditional Features/lablels.csv'
df_X = pd.read_csv(features_path)
df_Y = pd.read_csv(lables_path)

# X-> Features (2D array) ,   Y -> Labels (1D array)
X = np.array(df_X) # Features
Y = np.array(df_Y) # Labels


# clf -> 'SVM', 'KNN', 'MLP' 
clfs = ['SVM', 'KNN', 'MLP']
clf = clfs[2] # Classifier 
folds = 7 # No. of folds
print('Classifier : {}      No. of folds : {}'.format(clf, folds))

acc = cross_folds_results(X, Y, clf, folds)
print('Average of all folds : ', acc)

