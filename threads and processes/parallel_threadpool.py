# SuperFastPython.com
# example of a parallel for loop with the ThreadPool class
from multiprocessing.pool import ThreadPool
import time
import random


# execute a task
def task(value):
    # add your work here...
    # ...

    random_num = random.randrange(1, 20) 
    print(f'task {value} would like to sleep for {random_num} seconds')
    time.sleep(random_num)

    # return a result, if needed
    return value


# protect the entry point
if __name__ == '__main__':

    # create the pool with the default number of workers
    with ThreadPool() as pool:
        # issue one task for each call to the function
        for result in pool.map(task, range(100)):
            # handle the result
            print(f'>got {result}')

    # report that all tasks are completed
    print('Done')
