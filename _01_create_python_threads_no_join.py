'''
Creating Threads in Python without join

(c) www.xanthium.in

https://www.xanthium.in/creating-threads-sharing-synchronizing-data-using-queue-lock-semaphore-python

'''
import time
import threading   #required for threading 


def do_something():
    print(f'\nEntered do_something() ')
    time.sleep(2)
    print('\nDone Sleeping in thread\n')

    
print(f'\nStart of Main Thread ')

t1 = threading.Thread(target = do_something)   #create the thread t1
t1.start()                                     #start the threads

print('\nEnd of Main Thread\n+---------------------------+')