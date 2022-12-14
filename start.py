import os
import time
from multiprocessing import Process

folder = 'scripts'


def run_file(file_name):
    os.system(f'python ./{folder}/{file_name}')


if __name__ == '__main__':
    for file in os.listdir(f'./{folder}'):
        proc = Process(target=run_file, args=(file,))
        proc.start()
        time.sleep(.2)
