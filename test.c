#include "stdio.h"


int main(){
    int i;
    double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};
    for (i = 0; i <5;i++){
        printf ("%2f \n",balance[i]);
    }
    return 0;
}
