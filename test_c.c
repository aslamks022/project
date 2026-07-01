#include <stdio.h>
#include <assert.h>
#include "../c_utils/grade_convert.c"

void test_grade_s() {
    assert(get_grade(95.0) == 'S');
}
void test_grade_f() {
    assert(get_grade(45.0) == 'F');
}
