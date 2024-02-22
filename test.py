'''
Program to demonstrate the events in python threading

event.set()
event.wait() 

(c) www.xanthium.in
'''

import time
import threading

def infinite_loop_func():
    
    print('Thread-t1:Start the loop')

    while 1:
            
        if my_event.is_set():
            break
            
        print('Thread-t1:Read from Serial Port')
            
        time.sleep(1)
    
my_event = threading.Event()
my_event.clear()

t1 = threading.Thread(target = infinite_loop_func) # create t1 thread
t1.start()  

time.sleep(5)    #wait 5 seconds 

my_event.set()   #set the event after 5 seconds
print('\n[Event Set in Main Thread]')

t1.join()

print('\nEnd of the Main Thread')