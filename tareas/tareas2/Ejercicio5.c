#include <stdio.h>
#include "funciones4.h"
int main(void){
	int n;
	int n1;
	int op; 
	while(1) { 
		printf("\n   MENU DE OPERACIONES  \n");
		printf("1.- SUMA DE DOS NUMEROS\n"); 
		printf("2.- RESTA DE DOS NUMEROS\n");
		printf("3.- MULTIPLICACION DE  DOS NUMEROS \n"); 
		printf("4.- Salir\n");
		printf("Seleccione una opcion :  \n");
		scanf("%d", &op);  
		if(op == 4 ){ 
			printf("Usted ha seleccionado la opcion de salir de nuestro menu interactivo, gracias por su uso y nos vemos en la proxima :) \n"); 
			break; 
		 }
		 printf("Ingrese su primer numero para luego proceder a las operaciones\n "); 
		scanf("%d", &n);
		printf("Ingrese su segundo numero para luego proceder a las operaciones \n"); 
		scanf("%d", &n1); 
		switch(op){ 
			case 1: 
				printf("El resultado de la suma es :%d\n ", sumar(n,n1)); 
				break;
			case 2: 
				printf("El resultado de la resta es:%d\n ", restar(n,n1)); 
				break; 

			case 3:
				printf("El resultado de la multiplicacion es:%d \n", multiplicar(n,n1));  
				break; 
			default: 
				printf("La opcion que usted ha seleccionado es invalida, seleccione otra opcion nuevamente \n");


		} 




	 } 
	return 0; 



}
