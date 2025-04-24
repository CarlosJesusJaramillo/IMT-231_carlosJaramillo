#include <stdio.h>
#include "funciones.h"
int main(void){
	int n;
	int op; 
	while(1) { 
		printf("\n   MENU DE OPERACIONES  \n");
		printf("1.- Verificar si el numero es Primo\n"); 
		printf("2.- Calcular el factorial del numero");
		printf("3.- Contar numeros pares o impares entre 1 y n \n"); 
		printf("4.- Mostrar multiplos de 3 entre 1 y n  \n");	
		printf("5.- Salir\n");
		printf("Seleccione una opcion :  \n");
		scanf("%d", &op);  
		if(op == 5 ){ 
			printf("Usted ha seleccionado la opcion de salir de nuestro menu interactivo, gracias por su uso y nos vemos en la proxima :) \n"); 
			break; 
		 }
		printf("Ingrese su numero positivo para realizar alguna de nuestras operaciones: \n "); 
		scanf("%d", &n);
		if(n <= 0){ 
			printf("Error se ha ingresado un numero negativo, debe ingresar un numero positivo \n"); 
			continue; 
	         }

		switch(op){ 
			case 1:
				if (numprim(n)){ 
					printf("Su numero es primo \n ");

                                }else { 
					printf("Su numero no es primo  \n ");
				}
				
 
				break;
			case 2: 
				printf("El factorial de su numero es :%d\n ", factorial(n)); 
				break; 

			case 3:
				parimpar(n);  
				break; 
			case 4: 
				printf("Los numeros  multiplos de 3 desde 1 hasta el numero ingresado  %d  son:  \n   ",n);
				multiplos(n);
	

			default: 
				printf("La opcion que usted ha seleccionado es invalida, seleccione otra opcion nuevamente \n");


		} 




	 } 
	return 0; 

}

