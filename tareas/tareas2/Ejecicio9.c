#include <stdio.h>
#include "funciones8.h"
int main(void){
	int num;
	  
	while(1) {
		printf("Ingrese un numero:  \n");
        	scanf("%d", &num); 
		if(num => 0 && num <= 9){ 
				printf("Se han ingresado un numero que tiene solo 1 digito, a lo cual indica que nuestro sistema ha finaliado, gracias por su uso y hasta la proxima\n");
				break;  
		

		}
		int resultado = invn(num); 
		printf("El resultado del factorial es %d :\n" , resultado);
 

	 }  
	return 0; 



}
