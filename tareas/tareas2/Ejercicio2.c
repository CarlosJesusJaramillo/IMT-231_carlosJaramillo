#include <stdio.h>
#include "funciones1.h"
int main(void){
	int n;
	while(1) {
		printf("Ingrese un numero entero positivo :  \n");
        	scanf("%d", &n);
		if(n == 0){ 
			printf("EL programa ha finalizado con su funcion... \n");
			break; 
		 }else if(n <0){ 
			printf("Solo se deben ingresar solamente numeros entreros postivos \n" ) ;
			continue;
		 }
		int  cantidad =ContDig(n);
		printf("El numero tiene %d digitos \n", cantidad);


	 } 
	return 0; 



}
