#include <stdio.h>
#include "funciones5.h"


void comparar(int a,int b) {
    if (a > b){
	printf("El primer numero ingresado %d  es mayor que el segundo que es  %d\n", a, b);   
    }else if(a < b){
	printf("El primer numero ingresado %d es menor que el segundo que es %d\n", a, b);   
    }else {
	printf("El primer numero ingresado %d es igual al segundo que es  %d\n", a, b);    
    }
}

