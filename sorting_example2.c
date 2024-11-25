#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Δομή για την εγγραφή μαθητών
typedef struct {
    char name[50];
    int grade;
} Student;

// Συνάρτηση σύγκρισης για ταξινόμηση κατά βαθμό (φθίνουσα)
int compare_by_grade(const void* a, const void* b) {
    return ((Student*)b)->grade - ((Student*)a)->grade;
}

// Συνάρτηση σύγκρισης για ταξινόμηση κατά όνομα (αλφαβητικά)
int compare_by_name(const void* a, const void* b) {
    return strcmp(((Student*)a)->name, ((Student*)b)->name);
}

int main() {
    Student students[] = {
        {"Alice", 85},
        {"Bob", 92},
        {"Charlie", 78},
        {"David", 90}
    };
    int n = sizeof(students) / sizeof(students[0]);

    printf("Πριν την ταξινόμηση:\n");
    for (int i = 0; i < n; i++) {
        printf("%s - %d\n", students[i].name, students[i].grade);
    }

    // Ταξινόμηση κατά βαθμό (φθίνουσα σειρά)
    qsort(students, n, sizeof(Student), compare_by_grade);

    printf("\nΜετά την ταξινόμηση κατά βαθμό:\n");
    for (int i = 0; i < n; i++) {
        printf("%s - %d\n", students[i].name, students[i].grade);
    }

    // Ταξινόμηση κατά όνομα (αλφαβητικά)
    qsort(students, n, sizeof(Student), compare_by_name);

    printf("\nΜετά την ταξινόμηση κατά όνομα:\n");
    for (int i = 0; i < n; i++) {
        printf("%s - %d\n", students[i].name, students[i].grade);
    }

    return 0;
}
