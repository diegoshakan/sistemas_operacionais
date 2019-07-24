import signal
from time import sleep

def parar(x, y):
    print('''Eu não morro com sig
    tente com kill -9
    Digite o comando ps -aux para me identificar.
    Depois tente com o kill -9 e o meu PID''')

while True:
    print('Alô mundo cruel, vou dormir por um segundo.')
    sleep(1)
    signal.signal(signal.SIGINT, parar)