

#include<stdio.h>

int main() {
    int network[1000000000];
    network[55] = 123;
    network[57] = 456;
    printf("%d\n", network[55]);
    printf("Storage size for int : %d \n", sizeof(int));
//    for(int i=54; i<59; i++) {
//        printf("%d\n", network[i]);
//    }
}