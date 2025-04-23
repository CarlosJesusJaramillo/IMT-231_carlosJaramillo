#include <stdio.h>
typedef enum { ROJO, VERDE, AMARILLO } Semaforo;

int main() {
    Semaforo estado = ROJO; 
    int repeticiones = 0;

    while (repeticiones < 10) {
        
        switch (estado) {
            case ROJO:
                printf("Estado: ROJO - Detengase\n");
                estado = VERDE; 
                break;
            case VERDE:
                printf("Estado: VERDE - Avance y siga adelante\n");
                estado = AMARILLO;
                break;
            case AMARILLO:
                printf("Estado: AMARILLO - Precaución o tenga cuidado \n");
                estado = ROJO;
                break;
        }

        repeticiones++;
    }

    printf("El programa ha terminado con su funcion, despues de haber pasado los 10 ciclos.\n");
    return 0;
}
