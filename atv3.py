import signal
import os
from time import sleep

pid = os.getpid()
blefe = 0 

while True:
    print('Alô mundo cruel, vou dormir por um segundo.')
    sleep(1)
    blefe = blefe + 1
    if (blefe == 3):
        print('mamãe, só mais um pouquinho!')
        sleep(1)
        os.kill(pid, signal.SIGSTOP)
