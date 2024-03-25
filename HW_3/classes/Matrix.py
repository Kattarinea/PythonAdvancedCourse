import numpy as np
from HW_3.classes.HashMatrixMixin import HashMatrixMixin
from functools import lru_cache


class Matrix(HashMatrixMixin):
    _matrix: np.ndarray

    def __init__(self, matrix):
        self._matrix = matrix

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self._matrix + other._matrix)
        else:
            raise TypeError('Unsupported operand types')

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self._matrix * other._matrix)
        else:
            raise TypeError('Unsupported operand types')

    @lru_cache(maxsize=10)
    def __matmul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self._matrix @ other._matrix)
        else:
            raise TypeError('Unsupported operand types')

    def __str__(self):
        print(self._matrix)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return np.array_equal(self._matrix, other._matrix)
        else:
            raise TypeError('Unsupported operand types')

    def __hash__(self):
        return self.get_hash()

    def save_matrix(self, file_name):
        np.savetxt(fname=file_name, X=self._matrix)

    def get_matrix(self):
        return self._matrix

    def set_matrix(self, matrix):
        self._matrix = matrix
