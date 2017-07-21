from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


def classification(data_from_lead):
    # x são as entradas e y são as saídas
    x = np.genfromtxt('dataset.csv', delimiter=';', usecols=(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    y = np.genfromtxt('dataset.csv', delimiter=';', usecols=(22))
    print('The total number of examples in the dataset is: %d' % (len(x)))
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=42)
    print('The number of examples used for training are: %d' % (len(x_treino)))
    print('The number of examples used for testing are: %d' % (len(x_teste)))
    knn = KNeighborsClassifier(n_neighbors=24, p=2)
    knn.fit(x_treino, y_treino)
    print('The probability of the algorithm to be right is: %f%%' % (knn.score(x_teste, y_teste) * 100))
    print('Lead data:')
    print(data_from_lead)
    lead_status = knn.predict(data_from_lead)
    print('[0] unqualified\n[1] qualified')
    print('According to the lead data, his status is: %d' % (lead_status))
    return lead_status