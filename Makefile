CC = gcc
CFLAGS = -Wall -g

all: gpa_calc grade_convert file_handler report_gen

gpa_calc: gpa_calc.c
	  -o gpa_calc gpa_calc.c
grade_convert: grade_convert.c
	  -o grade_convert grade_convert.c
clean: rm -f gpa_calc grade_convert
