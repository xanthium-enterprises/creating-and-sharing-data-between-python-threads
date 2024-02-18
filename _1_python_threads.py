import time
import threading

def do_something():
    print(f'\nEntered the function do_something(){threading.current_thread()}')
    time.sleep(10)
    print('\nDone Sleeping')
    
print(f'\nStart of Main Thread {threading.current_thread() }')
t1 = threading.Thread(target = do_something)
t1.start()                                     #start the threads

print('\nEnd of Main Thread\n+---------------------------+')