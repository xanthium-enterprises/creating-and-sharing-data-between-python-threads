'''
Returning Values from Thread functions using Global Variables

(c) www.xanthium.in

'''
import time
import threading   #required for threading 

def add_two_numbers(no1,no2):
    global global_sum
    global_sum = no1 + no2
    #time.sleep(2)
    

    

global_sum = 0  # Global Value used to return data from thread 

print(f'Sum Intial Value -> {global_sum}')


First_No  = 5
Second_No = 10

t1 = threading.Thread(target = add_two_numbers,args=(First_No,Second_No))  # create the thread t1
t1.start()                                                                 # start the threads
t1.join()

print(f'Sum After Calculation-> {global_sum}')
