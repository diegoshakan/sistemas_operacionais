#include <pthread.h>
#include <stdio.h>
void *escreve(void *numero)
{
int *n =(int *) numero;
printf("Sistemas Operacionais thread n. = %d\n",*n);
pthread_exit(NULL);
}
void main()
{
pthread_t threads[3];
int s,i;
for (i=0; i<3; i++)
{
printf("A criar o thread n. %d\n",i);
s=pthread_create(&threads[i], NULL, escreve, (void *) &i); /* o valor de I se repete */
if (s)
{
perror("Erro ao criar o thread");
exit(-1);
}
}
pthread_exit(NULL); 
/* se a função main não terminar com a função phtread_exit o ultimo
thread não chega a terminar a sua execução */