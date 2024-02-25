'''
Program to display the name of the running threads.

(c) www.xanthium.in

Tutorial
https://www.xanthium.in/creating-threads-sharing-synchronizing-data-using-queue-lock-semaphore-python

'''

import threading


def do_something():
	print('Hello from Thread')
	print(threading.current_thread().name) #name of the thread
	print('\n')

def do_something_else():
	print('do_something_else')
	print(threading.current_thread().name)
	print('\n')
	
print(threading.current_thread().name)

t1 = threading.Thread(target = do_something).start()
t2 = threading.Thread(target = do_something_else).start()





