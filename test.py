import threading 

def do_something():
	#some statements here
	pass

t1 = threading.Thread(target = do_something)  #create the thread t1
t1.start()                                    #start the thread