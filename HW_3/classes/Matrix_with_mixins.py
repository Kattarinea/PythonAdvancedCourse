import numpy as np
from HW_3.classes.Matrix_Mixin import MatrixMixin


class MatrixWithMixins(MatrixMixin):

    def __add__(self, other):
        if isinstance(other, MatrixWithMixins):
            return MatrixWithMixins(self._matrix + other._matrix)
        else:
            raise TypeError('Unsupported operand types')

    def __mul__(self, other):
        if isinstance(other, MatrixWithMixins):
            return MatrixWithMixins(self._matrix * other._matrix)
        else:
            raise TypeError('Unsupported operand types')

    def __matmul__(self, other):
        if isinstance(other, MatrixWithMixins):
            return MatrixWithMixins(self._matrix @ other._matrix)
        else:
            raise TypeError('Unsupported operand types')


    def __eq__(self, other):
        if isinstance(other, MatrixWithMixins):
            return np.array_equal(self._matrix, other._matrix)
        else:
            raise TypeError('Unsupported operand types')
