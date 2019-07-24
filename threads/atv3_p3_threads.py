from time import sleep
from threading import *

class Task01(Thread):
    def run(self):        
        for i in range(5):
            sleep(0.5)
            print("Tarefa 01 - Rodando!")
            if i == 4:
                print("Tarefa 01 - Rodando!")
                print('Estou terminando e vou mandar um resultado para o programa principal')


t1 = Task01()
t1.start()
# sleep(0.2)
t1.join()

while True:
    sleep(0.5)
    print("Programa Principal")
    if t1._is_stopped == True:
        print("Programa Principal parou porque a thread apresentou um resultado.")
        break