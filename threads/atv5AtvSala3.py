import threading
import time

lista_soma = []
def soma(a, b):
    soma = a + b
    lista_soma.append(soma)
    print(f'{a} + {b} = {soma}')
    

lista_mult = []   
def mult(a, b):
    mult = a * b
    lista_mult.append(mult)
    print(f'{a} * {b} = {mult}')
    

thread1 = threading.Thread(target = soma, args = (3, 6))
thread1.start()
thread2 = threading.Thread(target = mult, args = (2, 8))
thread2.start()

print('Total de threads', threading.activeCount(), '(2 threads e o programa principal).')



thread1.join()
thread2.join()


resul_mult = lista_mult[0]
resul_soma = lista_soma[0]

soma_threads = resul_soma + resul_mult
print(f'thread 1 + thread 2 = {soma_threads}')
