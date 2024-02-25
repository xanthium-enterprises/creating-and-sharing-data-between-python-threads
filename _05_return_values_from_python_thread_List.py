'''
Returning Values from Thread functions using a List direct access by the thread

https://www.xanthium.in/creating-threads-sharing-synchronizing-data-using-queue-lock-semaphore-python

(c) www.xanthium.in

'''
import time
import threading   #required for threading 

def append_list_thread():
    global_list.append('Appended in append_list_thread()')



global_list = [] #Create empty global list
global_list.append('Appended in Main Thread')

print(global_list)

t1 = threading.Thread(target = append_list_thread)
t1.start()
t1.join()

print(global_list)