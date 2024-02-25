import threading


def do_something():
	print('Hello from Thread')
	print(threading.current_thread().name)
	print('\n')

def do_something_else():
	print('do_something_else')
	print(threading.current_thread().name)
	print('\n')
	
print(threading.current_thread().name)

t1 = threading.Thread(target = do_something).start()
t2 = threading.Thread(target = do_something_else).start()





