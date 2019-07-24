// Programa sinal4.cpp
// Sinais são eventos gerados pelo Unix em resposta a algumas condi��es:
//  erros, violação de memória, ...


// Processo mandando um alarme
// 

#include <signal.h> // definição dos sinais de interrupções
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>




void alarme (int sig)
{
  
  kill(getpid(),SIGKILL);
}

int main()
{
  int cont=1;

  int pai = 1;
  // o processo filho espera por 5 segundos antes de enviar um sinal SIGALRM para seu pai

  int pid;
 

  printf("O alarme foi disparado. \n");
while(1){
  if ( (pid = fork()) == 0)
  {
    // c�digo do processo filho
    printf("\n\n           Filho vai dormir por 5 segundos\n");
    sleep(5);
    if (cont == 3){
      kill(getppid(), SIGALRM);
      pai = 0;
      printf("Pai morreu, mas eu não. Vivinho da Silva \n");
    }
    cont+=1;
  }
  else{
    if(pai){
      printf("Pai esperando pelo Sinal \n");
      (void) signal(SIGALRM, alarme);
      printf("Ninguém pode me matar! hehehe \n");
      pause();
      printf("Eita, morri!");
    }
  }
}
}
