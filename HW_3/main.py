import argparse

import numpy as np

from Paths_to_artifacts import PathsToArtifacts
from classes.Matrix import Matrix
from classes.Matrix_with_mixins import MatrixWithMixins


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn_sum', default='matrix+.txt', help='Имя файла для суммы матриц')
    parser.add_argument('-fn_prod', default='matrix_prod.txt',  # Нельзя создать файл с символом *
                        help='Имя файла для матричного произведения')
    parser.add_argument('-fn_comp_prod', default='matrix@.txt',
                        help='Имя файла для покомпонентного произведения матриц')
    parser.add_argument('-task', type=int, default=1, help='Номер задания')
    parser.add_argument('-seed', default=0, type=int, help='seed для генерации')
    parser.add_argument('-A', default='A.txt', help='Имя файла для матрицы А из задания 3')
    parser.add_argument('-B', default='B.txt', help='Имя файла для матрицы B из задания 3')
    parser.add_argument('-C', default='C.txt', help='Имя файла для матрицы C из задания 3')
    parser.add_argument('-D', default='D.txt', help='Имя файла для матрицы D из задания 3')
    parser.add_argument('-AB', default='AB.txt', help='Имя файла для A @ B из задания 3')
    parser.add_argument('-CD', default='CD.txt', help='Имя файла для C @ D из задания 3')
    parser.add_argument('-hash', default='hash.txt', help='Имя файла для hash AB и CD из задания 3')
    return parser.parse_args()


def check_args(l_args):
    return l_args.task in [1, 2, 3]


def create_artifacts_1_2(path_to_dir, l_args):
    np.random.seed(args.seed)
    task = l_args.task
    matrix1 = create_matrix(task)
    matrix2 = create_matrix(task)

    sum_matrix = matrix1 + matrix2
    mat_prod_matrix = matrix1 * matrix2
    comp_prod_matrix = matrix1 @ matrix2

    sum_matrix.save_matrix(path_to_dir + l_args.fn_sum)
    mat_prod_matrix.save_matrix(path_to_dir + l_args.fn_prod)
    comp_prod_matrix.save_matrix(path_to_dir + l_args.fn_comp_prod)


def create_matrix(task: int):
    array = np.random.randint(0, 10, (10, 10))
    if task == 1:
        matrix = Matrix(array)
    else:
        matrix = MatrixWithMixins(array)
    return matrix


def first_task(l_args):
    path_to_dir = PathsToArtifacts.PATH_TO_TASK_1.value
    create_artifacts_1_2(path_to_dir=path_to_dir, l_args=l_args)


def second_task(l_args):
    path_to_dir = PathsToArtifacts.PATH_TO_TASK_2.value
    create_artifacts_1_2(path_to_dir=path_to_dir, l_args=l_args)


def third_task(l_args):
    path_to_dir = PathsToArtifacts.PATH_TO_TASK_3.value
    a, b, c, d = init_matrix_task3()
    if (hash(a) == hash(c)) and (a != c) and (b == d) and (a @ b != c @ d):
        a.save_matrix(path_to_dir + l_args.A)
        b.save_matrix(path_to_dir + l_args.B)
        c.save_matrix(path_to_dir + l_args.C)
        d.save_matrix(path_to_dir + l_args.D)
        ab = a @ b
        ab.save_matrix(path_to_dir + l_args.AB)
        cd = c @ d
        cd.save_matrix(path_to_dir + l_args.CD)
        with open(path_to_dir + l_args.hash, 'w+') as file:
            file.write(f'{hash(ab)}\n{hash(cd)}')


def init_matrix_task3():
    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], )
    c = np.array([[0, 3, 2],
                  [5, 4, 7],
                  [6, 9, 9]
                  ])
    b = np.array([[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]
                  ])
    d = np.array([[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]
                  ])
    return Matrix(a), Matrix(b), Matrix(c), Matrix(d)


if __name__ == '__main__':
    args = get_args()
    if check_args(args):
        if args.task == 1:
            first_task(l_args=args)
        elif args.task == 2:
            second_task(l_args=args)
        elif args.task == 3:
            third_task(l_args=args)
