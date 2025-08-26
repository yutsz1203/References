/*
C++ is a statically typed langauge, which means that is uses static styping to determine data types and
perform type checking during compile time. This helps with ensuring type safety and prevent
certain types of errors from occuring during the execution of the program.
*/
#include <iostream>

int main(){
    int num = 65;
    double pi = 3.14159;
    char c = 'c';

    c = num; // convert num's value to ASCII equivalent character
    num = pi; // convert pi's value from double type to int type

    std::cout << "The value of num is: " << num << "\n";
    std::cout << "The value of pi is: " << pi << "\n";
    std::cout << "The value of c is: " << c << "\n";
    return 0;
}