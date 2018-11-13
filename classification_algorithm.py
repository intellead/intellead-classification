from enum import Enum
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


class ClassificationAlgorithm(Enum):
    DT = DecisionTreeClassifier(max_depth=7)
    KNN = KNeighborsClassifier(n_neighbors=7, p=2)
    AB = AdaBoostClassifier()
    RF = RandomForestClassifier(max_depth=23, n_estimators=10, max_features=1)
    MLP = MLPClassifier(alpha=1)
    QDA = QuadraticDiscriminantAnalysis()
    GNB = GaussianNB(),
    SVC = SVC(gamma=2, C=1),
    LSVC = SVC(kernel="linear", C=0.025)
