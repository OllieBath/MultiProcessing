import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('done sleeping')

processes = []

for _ in range(5):
    p = multiprocessing.Process(target=do_something, args=[2])
    p.start()
    processes.append(p)

for process in processes:
    process.join()


finish = time.perf_counter()

print(f'finished in {round(finish-start, 2)} second(s)')