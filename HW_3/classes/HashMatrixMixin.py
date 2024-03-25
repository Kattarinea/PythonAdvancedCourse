import numpy as np


class HashMatrixMixin:

    def get_hash(self):
        return int(np.sum(self._matrix))  # Считается сумма всех элементов матрицы
