import threading
import time

def display_numbers():
    for i in range(1, 6):
        print("\nNumber:", i)
        time.sleep(4)

def display_squares():
    for i in range(1, 6):
        print("\nSquare of", i, "=", i * i)
        time.sleep(4)

def display_messages():
    for i in range(1, 6):
        print("\nPython Thread:", i)
        time.sleep(4)

t1 = threading.Thread(target=display_numbers)
t2 = threading.Thread(target=display_squares)
t3 = threading.Thread(target=display_messages)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All tasks completed.")
