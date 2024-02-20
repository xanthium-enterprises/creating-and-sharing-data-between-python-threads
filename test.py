'''


(c) www.xanthium.in

'''

import time
import threading   #required for threading 

character_array = []

def append_A():
    for i in range(10):
       character_array.append('A')
       time.sleep(2)
    #print(integer_array)


def append_B():
    for i in range(10):
       character_array.append('B') 
       time.sleep(6)
    #print(integer_array)


t1= threading.Thread(target = append_A)
t2= threading.Thread(target = append_B)

t1.start()
t2.start()

t1.join()
t2.join()

print(character_array)
