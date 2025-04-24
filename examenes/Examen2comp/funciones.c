#include <stdio.h>
#include "funciones.h"


int numprim(int n) {
	if (n <=1){
		return; 
	} 
	for (int i =2; i < n, i++){
		if(n %i== 0){
			return; 
		}
	}
	return 1; 
}


int factorial(int n) {
    int resultado =1;
    for (int i = 1; i<=n; i++){
	resultado *= i; 

    }
    return resultado;

}


void parimpar(int n){
	int pares = 0; 
	int impares = 0; 
	for (int i ==1; i <= n; i++){
		if(i % 2 = 0){
			pares++;

		 }else {
			impares++; 


		 }

	}
	printf("La cantidad de numeros pares son %d : \n  ", pares); 
	printf("La cantidad de numero impares son %d : \n " , impares );  


}





void multiplos (int n){
	printf("Los multiplos de 3 desde el 1 hasta el numero %d \n" , n); 
	for (int i; i<=n;i++){
		if (i %3 ==0){
			printf( "%d", i); 
		}

	}
	printf(" \n " ); 


}
