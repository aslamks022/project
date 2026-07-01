#include <stdio.h>

char get_grade(float score) {
    // Convert score to grade
    if(score >= 90) {
        return 'S';
    }
    else if(score >= 80) {
        return 'A';
    }
    else if(score >= 70) {
        return 'B';
    }
    else if(score >= 60) {
        return 'C';
    }
    else if(score >= 50) {
        return 'D';
    }
    else {
        return 'F';
    }
}

int main(){ printf("%c", get_grade(85.5)); return 0; }
