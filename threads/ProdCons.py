from threading import Thread, Condition
from time import sleep
from random import choices

list_numbers = []
len_list = 10
cond = Condition()
random_numbers = range(1,10)

class Producer(Thread):
    def run(self):
        global list_numbers
        global random_numbers
        while True:
            cond.acquire()
            if len(list_numbers) == 10:
                print('Fora de Tempo')
                cond.wait()
                print('Tempo Igual')
            choose = choices(random_numbers)
            list_numbers.append(choose)
            print(f'producing: {choose}')
            cond.notify()
            cond.release()
            sleep(choices(random_numbers)[0]/10)

class Consumer(Thread):
    def run(self):
        global list_numbers
        while True:
            cond.acquire()
            if not list_numbers:
                print('Producer Avançou, Esperando')
                cond.wait()
                print('Consumer - Tempo Igual')
            num = list_numbers.pop(0)
            print(f'consuming: {num}')
            cond.notify()
            cond.release()
            sleep(choices(random_numbers)[0]/5)

Producer().start()
Consumer().start()

