'''
Program to demonstrate the locks in python threading
using 
 
 lock.acquire()
 lock.release()

(c) www.xanthium.in

'''

import time
import threading


def update_list_A(var_list):       #function to write A's to the List
    print('update_list_A thread called ')
    
    lock.acquire()             #acquire the lock,other threads are not allowed to access the threadduring lock

    for _ in range(10):
        var_list.append('A')
        time.sleep(0.10)
    
    lock.release()
    
        
    
def update_list_B(var_list): #function to write B's to the List
    print('update_list_B thread called ')
    
    #lock.acquire()
    
    for _ in range(10):
        var_list.append('B')
        time.sleep(0.10)

    #lock.release()

lock = threading.Lock()


shared_list =[] #Shared variable to be modified in threads


t1 = threading.Thread(target = update_list_A, args = (shared_list,))
t2 = threading.Thread(target = update_list_B, args = (shared_list,))


t1.start()
t2.start()


t1.join()
t2.join()

print(f'\n{shared_list}')
print('\nEnd of Main Thread\n')


