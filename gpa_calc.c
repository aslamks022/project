#include <stdio.h>
#include <stdlib.h>

// GPA Calculator for Student Performance
int main() {
    int n;
    float marks[50];
    float sum = 0.0;
    float gpa;

    printf("Enter number of subjects: ");
    scanf("%d", &n);

    printf("Enter marks: \n");
    for(int i = 0; i < n; i++) {
        printf("Subject %d: ", i+1);
        scanf("%f", &marks[i]);
    }

    for(int i = 0; i < n; i++) {
        sum += marks[i];
    }

    gpa = (sum / n) / 10;
    printf("Total Marks: %.2f\n", sum);
    printf("Percentage: %.2f%%\n", sum/n);
    printf("GPA: %.2f\n", gpa);

    return 0;
}
