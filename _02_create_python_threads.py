'''
Creating Threads in Python with join

(c) www.xanthium.in

'''
import time
import threading   #required for threading 

def do_something():
    print(f'\nEntered do_something() ')
    time.sleep(2)
    print('\nDone Sleeping in Thread\n')

    
print(f'\nStart of Main Thread ')

t1 = threading.Thread(target = do_something)   #create the thread t1
t1.start()                                     #start the threads
t1.join()

print('\nEnd of Main Thread\n+---------------------------+')