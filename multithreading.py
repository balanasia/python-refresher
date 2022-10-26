# thread = a flow of execution. Like a separate order of instructions
#          However each thread takes a turn running to archieve concurrency
#          GIL = (global interpreter lock)
#          allows only one thread to hold control of python interpreter

# cpu bound = program/task spends most of it's time aiting for interval events (CPU intensive)
#             use multiprocessing
#
# io bound = program/task spends most of it's time waiting for external events (user input)
#            use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def do_homework():
    time.sleep(5)
    print("You finish study")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=do_homework, args=())
z.start()

# thread sync
x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# do_homework()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())