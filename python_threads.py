import time
import threading

def do_something():
    print('Entered the function do_something()')
    time.sleep(1)
    print('Done Sleeping')
    

t1 = threading.Thread(target = do_something)
t1.start()                                     #start the threads

print('\nEnd of Main Thread')