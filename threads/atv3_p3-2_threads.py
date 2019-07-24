import threading
import time
 
def task(msg):
    while True:
    # for i in range(5):
        print(msg)
        time.sleep(1)
 
 
t = threading.Thread(target=task,args=("thread sendo executada",))
t.start()
while t.isAlive():
    print ("Aguardando thread")
    time.sleep(1)