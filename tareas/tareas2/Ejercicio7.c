#include <stdio.h>
#include "funciones6.h"
int main(void){
	int num;
	int contador = 0;  
	while(1) {
		printf("Ingrese un numero:  \n");
        	scanf("%d", &num); 
		if(num ==-1){ 
				printf("Se han ingresado un -1 a lo cual indica que nuestro sistema ha finaliado, gracias por su uso y hasta la proxima\n");
				break;  
		

		}if(multiplo3(num)){ 
			contador++; 


		}
		

	 } 
	printf("El total de los multiplos de 3 ingresados son : %d \n", contador); 
	return 0; 



}
