/* 
Reference: 
https://www.programiz.com/cpp-programming/type-conversion

C++ is a statically typed langauge, which means that is uses static styping to determine data types and
perform type checking during compile time. This helps with ensuring type safety and prevent
certain types of errors from occuring during the execution of the program.

Data Loss during conversion
long -> int -> short -> char
long double -> double -> float

*/

#include <iostream>
using namespace std;

int main(){
    // Implicit Type Conversion (automatic conversion)
    int num_int = 9;
    double num_double;

    // assigning int value to a double variable
    num_double = num_int;

    cout << "num_int = " << num_int << endl; // 9
    cout << "num_double = " << num_double << endl; // 9, not 9.0

    // assigning double value to a int variable
    num_double = 9.99;
    num_int = num_double;

    cout << "num_int = " << num_int << endl; // 9
    cout << "num_double = " << num_double << endl; // 9.99

    // Explicit Conversion

    // C-style Type Casting
    num_double = (double)num_int;

    // Function-style Casting
    num_double = double(num_int);
    return 0;
}