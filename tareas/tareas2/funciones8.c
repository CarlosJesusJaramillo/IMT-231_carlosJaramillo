#include <stdio.h>
#include "funciones8.h"


int numinv(int n) {
    int invertido =0;
    while(n>0){
	int digito = n % 10; 
	invertido = invertido * 10 +digito;
	n /=10; 

    }
    return invertido;

}
