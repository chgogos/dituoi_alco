#include <stdio.h>

int max_array_r(int *a, int n) {
  if (n == 1) {
    return a[0];
  } else {
    int rm = max_array_r(a, n - 1);
    return (rm > a[n - 1]) ? rm : a[n - 1];
  }
}

int main() {
  int a[] = {4, 5, 2, 8, 1, 6};
  int max = max_array_r(a, sizeof(a) / sizeof(int));
  printf("Max = %d\n", max);
}