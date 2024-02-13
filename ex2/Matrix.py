import numpy as np
from scipy.spatial.distance import cdist

def solution(A, B, k):
    distances = cdist(A, B, 'euclidean')
    nearest_indices = np.argsort(distances, axis=0)[:k]+1
    return nearest_indices.T

"Введем данные для примера"
A = np.array([[0, 0], [1, 0], [2, 0]])
B = np.array([[0, 1], [2, 1]])
C = solution(A, B, 3)
print(C)