import numpy as np


class MatrixMixin:
    _matrix: np.ndarray

    def __init__(self, matrix):
        self._matrix = matrix

    def __hash__(self):
        return int(np.sum(self._matrix))

    def __str__(self):
        print(self._matrix)

    def save_matrix(self, file_name):
        np.savetxt(fname=file_name, X=self._matrix)

    def get_matrix(self):
        return self._matrix

    def set_matrix(self, matrix):
        self._matrix = matrix
