#include <stdio.h>

int max_r(int a[], int n){
    if (n==1){
        return a[0];
    }
    else{
        int temp = max_r(a, n-1);
        return temp>a[n-1]?temp:a[n-1];
    }
}

int main(){
    int a[] ={4, 2, 7, 8, 1, 9, 0};
    int x = max_r(a, 7);
    printf("max=%d\n", x);
}