'''
Program to demonstrate producer-consumer problem in python

one producer -> one consumer

(c) www.xanthium.in
'''

import time
import threading
import queue       #thread safe queue

def producer(shared_buffer):

    for i in range(10):
        shared_buffer.put(i)
        time.sleep(1)
    
    shared_buffer.put(None)
    
def consumer(shared_buffer):
    while True :
        rxed_data = shared_buffer.get()

        if rxed_data == None:
            break
       
        print(rxed_data)

    
shared_buffer = queue.Queue() #create a thread safe queue

t1 = threading.Thread(target = producer,args = (shared_buffer,))
t2 = threading.Thread(target = consumer,args = (shared_buffer,))

t1.start()
t2.start()

t1.join()
t1.join()