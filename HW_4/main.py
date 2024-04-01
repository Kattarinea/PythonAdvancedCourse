from Threading_and_multiprocessing import fibonacci, run_with_threads, run_with_processes
from Path_to_artifacts import PathsToArtifacts

if __name__ == '__main__':
    average_thread_time = 0
    average_process_time = 0

    Sync_time = fibonacci(1000000)
    print('Sync completed')

    for _ in range(10):
        average_thread_time += run_with_threads(1000000)
    average_thread_time /= 10
    print('Thread completed')

    for _ in range(10):
        average_process_time += run_with_processes(1000000)
    average_process_time /= 10
    print('Process completed')

    path = PathsToArtifacts.PATH_TO_ARTIFACTS.value + 'fibonacci_time.txt'
    with open(path, 'w') as file:
        file.write(f'Sync execution time: {Sync_time} seconds\n')
        file.write(f'Thread execution time: {average_thread_time} seconds\n')
        file.write(f'Process execution time: {average_process_time} seconds\n')
