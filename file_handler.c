#include <stdio.h>
#include <string.h>

void write_marks(char usn[], float marks[], int n) {
    FILE *fp;
    fp = fopen("marks.txt", "a");
    if(fp == NULL) {
        printf("Error opening file");
        return;
    }
    fprintf(fp, "%s ", usn);
    for(int i = 0; i < n; i++) {
        fprintf(fp, "%.2f ", marks[i]);
    }
    fprintf(fp, "\n");
    fclose(fp);
}

void read_marks() {
    FILE *fp = fopen("marks.txt", "r");
    char line[256];
    while(fgets(line, sizeof(line), fp)) {
        printf("%s", line);
    }
    fclose(fp); }
