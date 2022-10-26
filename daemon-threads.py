# deamon thread = a thread that runs in the background, not import to the program
#                 your program will not wait for daemon threads to complete before exiting
#                 non-dameon threads cannot normally be killed, stay alive until the task is complete
#
#                 background tasks, garbage collection, waiting for input, long running process etc

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for ", count, " seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

print(x.isDaemon())

answer = input("Do you wish to exit?")
