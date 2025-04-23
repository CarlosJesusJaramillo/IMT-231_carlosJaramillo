#include <stdio.h>
#include "funciones1.h"


int ContDig(int a) {
    int contador = 0;
    while (a != 0) {
	a /=10; 
	contador++;
    } 
    return contador; 
    
}
