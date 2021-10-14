import numpy as np
from numpy import array
import sklearn.svm
from sklearn.neural_network import MLPClassifier as MLP
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, balanced_accuracy_score,confusion_matrix
from sklearn.model_selection import KFold

def classification_accuracy(labels, predictions):
    #correct = np.where(labels == predictions)
    correct = 0
    for i in range(len(labels)):
        if labels[i][0] == predictions[i] :
            correct+=1
    #print('correct : ', correct)
    accuracy = correct/len(labels)
    return accuracy

def classification(X_train, Y_train, X_test, Y_test, classifier = 'SVM'):
    if classifier == 'SVM':
        clf = sklearn.svm.SVC(kernel='linear',gamma='scale',C=5)
    elif classifier == 'MLP':
        clf = MLP(activation = 'tanh',solver = 'lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    elif classifier == 'KNN':
        clf = KNN(n_neighbors=3)

    clf.fit(X_train, Y_train)
    predictions = clf.predict(X_test)
    #print('test labels : ', Y_test)
    #print('Predictions : ', predictions)
    accuracy = classification_accuracy(Y_test, predictions)

    return accuracy


def cross_folds_results(X, Y, classifier = 'SVM', Fold = 5):
    #X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.33, random_state=42)
    kfold = KFold(Fold, True, 1)
    total_acc = 0
    fold_count = 0
    for train_index, test_index in kfold.split(X):
        X_train, X_test, Y_train, Y_test = X[train_index], X[test_index], Y[train_index], Y[test_index]
        #print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)
        temp_acc = classification(X_train, Y_train, X_test, Y_test, classifier)
        total_acc += temp_acc
        fold_count += 1
        print('Fold no: {}     accuracy: {}'.format(fold_count, temp_acc))
    return total_acc/Fold
    