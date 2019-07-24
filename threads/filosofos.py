import random
import threading
import time
 
class Filosofo(threading.Thread):
 
    jantar = True
 
    def __init__(self, nome_profeta, garfo_esquerdo, garfo_direito):
        threading.Thread.__init__(self)
        self.nome = nome_profeta
        self.garfo_esquerdo = garfo_esquerdo
        self.garfo_direito = garfo_direito
 
    def run(self):
        while(self.jantar):
            time.sleep( random.uniform(3,13))
            print(f'{self.nome} está com fome.')
            self.comer()
 
    def comer(self):
        garfo1, garfo2 = self.garfo_esquerdo, self.garfo_direito
 
        while self.jantar:
            garfo1.acquire(True)
            locked = garfo2.acquire(False)
            if locked: break
            garfo1.release()
            print(f'{self.nome} troca garfo.')
            garfo1, garfo2 = garfo2, garfo1
        else:
            return
 
        self.jantando()
        garfo2.release()
        garfo1.release()
 
    def jantando(self):			
        print(f'{self.nome} começou a comer.')
        time.sleep(random.uniform(1,10))
        print (f'{self.nome} terminou de comer e voltou a refletir.')
 
def jantar_filosofos():
    filosofos_nomes = ('Tiririca','Dilma','Bam Bam','Seu Lunga', 'Bolsonaro')
    tam_filosofos_nomes = len(filosofos_nomes)
    garfos = [threading.Lock() for n in range(tam_filosofos_nomes)]
    Filosofos= [Filosofo(filosofos_nomes[i], garfos[i%5], garfos[(i+1)%5]) \
            for i in range(tam_filosofos_nomes)]
 
    random.seed(57129)
    Filosofo.jantar = True
    for p in Filosofos: p.start()
    time.sleep(100)
    Filosofo.jantar = False
    print ("Agora estamos satisfeitos!")
 
jantar_filosofos()
