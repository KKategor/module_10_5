# Task "Многопроцессное программирование"

from datetime import datetime
from multiprocessing import Pool

def read_info(filenames):
    all_data = []
    for name in filenames:
        with open (name, 'r', encoding= 'utf-8') as file:
            for line in file:
                all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    read_info(filenames)
    print(datetime.now() - start_time, 'линейный метод')

    start_time = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(datetime.now() - start_time, 'многопроцессный метод')