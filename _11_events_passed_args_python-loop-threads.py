'''
Program to demonstrate the events in python threading
Stop an infinite loop using Events
Event passed as args into thread function 

event.set()
event.wait() 

(c) www.xanthium.in
'''

import time
import threading

def infinite_loop_func(event_state):
    
    print('Thread-t1:Start the loop')

    while 1:
            
        if event_state.is_set():
            break
            
        print('Thread-t1:Read from Serial Port')
            
        time.sleep(1)

    print(f'Thread-t1: my_event.is_set() = {event_state.is_set()}')
    
my_event = threading.Event()
my_event.clear()

t1 = threading.Thread(target = infinite_loop_func,args =(my_event,)) # create t1 thread
t1.start()  

time.sleep(5)    #wait 5 seconds 

my_event.set()   #set the event after 5 seconds
print('\n[Event Set in Main Thread]')

t1.join()

print('\nEnd of the Main Thread')