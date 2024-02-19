'''
Passing Arguments into functions

(c) www.xanthium.in

'''
import time
import threading   #required for threading 

def do_something(myarg1):
    print(f'Arguments inside thread ->{myarg1}')
    time.sleep(2)
    

    
print(f'\nStart of Main Thread ')

t1 = threading.Thread(target = do_something,args = (1,))  #create the thread t1
t1.start()                                     #start the threads
t1.join()

print('\nEnd of Main Thread\n+---------------------------+')