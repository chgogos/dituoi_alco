#include <stdio.h>
#include <stdlib.h>

// Συνάρτηση σύγκρισης για αύξουσα ταξινόμηση
int compare(const void *a, const void *b) { return (*(int *)a - *(int *)b); }

int main() {
  int arr[] = {42, 17, 8, 99, 23};
  int n = sizeof(arr) / sizeof(arr[0]);

  printf("Πριν την ταξινόμηση:\n");
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");

  // Ταξινόμηση με qsort
  qsort(arr, n, sizeof(int), compare);

  printf("Μετά την ταξινόμηση:\n");
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");

  return 0;
}
