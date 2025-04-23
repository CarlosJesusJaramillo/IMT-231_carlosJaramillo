#include <stdio.h>
#include "funciones3.h"
int main(void){
	int n;
	int suma=0; 
	while(1) {
		printf("Ingrese un numero entero positivo :  \n");
        	scanf("%d", &n);
		if(n < 0){ 
			printf("EL programa ha finalizado con su funcion... \n");
			printf("El resultado de la suma total  es:  %d\n", suma);  
			break; 
		 }else if(n == 0){ 
			printf("Solo se deben ingresar solamente numeros entreros postivos, siendo el caso de 0 no lo es \n" ) ;
			continue;
		 }
		suma = acumular(suma,n);


	 } 
	return 0; 



}
