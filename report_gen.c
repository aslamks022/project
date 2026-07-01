#include <stdio.h>
#include <time.h>

void generate_student_report(char name[], char usn[], float gpa) {
    FILE *fp;
    time_t t;
    time(&t);

    fp = fopen("report.txt", "w");
    if(fp == NULL) return;

    fprintf(fp, "============================\n");
    fprintf(fp, "   STUDENT REPORT CARD\n");
    fprintf(fp, "============================\n");
    fprintf(fp, "Date: %s", ctime(&t));
    fprintf(fp, "Name: %s\n", name);
    fprintf(fp, "USN: %s\n", usn);
    fprintf(fp, "GPA: %.2f\n", gpa);
    fprintf(fp, "Grade: %c\n", gpa>=9?'S':gpa>=8?'A':'B');
    fprintf(fp, "============================\n");
    fclose(fp);
    printf("Report generated: report.txt\n");
}

int main(){ generate_student_report("Test User", "1CR21CS001", 8.75); }
