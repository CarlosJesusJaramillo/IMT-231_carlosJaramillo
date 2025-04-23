#include <stdio.h>
#include "funciones7.h"
int main(void){
	int num;
	  
	while(1) {
		printf("Ingrese un numero:  \n");
        	scanf("%d", &num); 
		if(num <= 0){ 
				printf("Se han ingresado un numero cero o menor a este, a lo cual indica que nuestro sistema ha finaliado, gracias por su uso y hasta la proxima\n");
				break;  
		

		}
		int resultado = factorial(num); 
		printf("El resultado del factorial es %d :\n" , resultado);
 

	 }  
	return 0; 



}
