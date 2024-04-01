import threading
import multiprocessing
from timing_decorator import timing


@timing
def fibonacci(n):
    if n <= 0:
        return 0

    if n == 1:
        return 0

    f1 = f2 = 1

    for i in range(2, n):
        f1, f2 = f2, f1 + f2


def fibonacci_worker(n):
    return fibonacci(n)


@timing
def run_with_threads(n):
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fibonacci_worker, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


@timing
def run_with_processes(n):
    processes = []

    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci_worker, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
