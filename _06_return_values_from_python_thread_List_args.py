'''
Returning Values from Thread functions using a List 
using an argument on threading.Thread(target,args = (global_list,) )

https://www.xanthium.in/creating-threads-sharing-synchronizing-data-using-queue-lock-semaphore-python

(c) www.xanthium.in

'''
import time
import threading  

def append_list_thread(list_to_be_appended):
   list_to_be_appended.append('Appended in append_list_thread()')
   
global_list = [] #Create empty global list

global_list.append('Appended in Main Thread')

print(global_list) #before calling the thread

t1 = threading.Thread(target = append_list_thread,args = (global_list,) )
t1.start()
t1.join()

print(global_list) #after calling the thread