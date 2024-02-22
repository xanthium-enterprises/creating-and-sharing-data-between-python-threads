'''
Program to demonstrate the events in python threading

event.set()
event.wait() 

(c) www.xanthium.in
'''

import time
import threading

def function_t(): 

    print('Entered t1 thread func')

    my_event.wait()      # wait for the event to be set in main thread

    print('Event is set,so this line gets printed')
    

my_event = threading.Event()               # create an Event object 

t1 = threading.Thread(target = function_t) # create t1 thread
t1.start()                                 # start  t1 thread

print('will set the event in 5 seconds')

time.sleep(5)    #wait 5 seconds 
my_event.set()   #set the event after 5 seconds

t1.join()

    

