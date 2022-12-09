import os
import time
from multiprocessing import Process


def run_file(file_name):
    os.system(f'python ./scripts/{file_name}')


if __name__ == '__main__':
    for file in os.listdir('./scripts'):
        proc = Process(target=run_file, args=(file,))
        proc.start()
        time.sleep(1)
