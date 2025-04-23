#include <stdio.h>
#include "funciones5.h"
int main(void){
	int num1;
	int num2; 
	while(1) {
		printf("Ingrese un numero entero positivo :  \n");
        	scanf("%d", &num1);
		printf("Ingrese el segundo numero entero:\n"); 
		scanf("%d", &num2); 
		if(num1 == 0 && num2 == 0){ 
				printf("Se han ingresado dos ceros, lo que equivale que el sistema ha terminado con su funcion, gracias por su uso y hasta la proxima\n");
				break;  
		

		}
		comparar(num1,num2); 

	 } 
	return 0; 



}
