#include <stdio.h>
#include "funciones.h"
int main(void){
	int n;
	while(1) {
		printf("Ingrese un numero :  \n");
        	scanf("%d", &n);
		if(n == -1){ 
			printf("EL programa ha finalizado con su funcion... \n");
			break; 
		 }if (parImpar(n)){ 
			printf(" ES PAR\n" ) ;


		 }else{ 
			printf(" ES IMPAR\n" ) ;


		 } 
	}

	return 0; 



}
