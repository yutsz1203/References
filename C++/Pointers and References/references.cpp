// Lvalues: those that evaluate to functions or identifiable objects (including variables) that persist beyond the end of the expression.
// Rvalues: those that evaluate to values, including literals and temporary objects that do not persist beyond the end of the expression.
// pass by reference can avoid making an expensive copy of an argument when calling a function
// pass by reference to non-const allows us to write functions that modify the value of arguments passed in

/*
Pass by value: fundamental types and enumerated types
Pass by const reference: Class types, and when not sure what to do
Pass by reference: Need modify values
*/
#include <iostream>

// only accept non-const lvalues here
void swap(int& a, int& b){
    int temp = a;
    a = b;
    b = temp;
}

// accept moddifiable lvalues, non-modifiable lvalues, and rvalues.
void printRef(const int& y){
    std::cout << y << '\n';
}

// string parameter, std::string_view is the string version of pass by reference, >= c++14 
void doSomething(const std::string_view){
    return;
}

int main(){
    // lvalue references
    int val = 10;
    int& ref = val;

    std::cout << val << std::endl; // 10
    ref = 20;
    std::cout << val << std::endl; // 20

    int x = 1;
    int y = 2;

    std::cout << "Before swapping: " << x << " " << y << std::endl; // 1 2

    swap(x, y);
 
    std::cout << "After swapping: " << x << " " << y << std::endl; // 2 1

    // lvalue references to const
    const int c1 = 1;
    const int& constref1 = c1;

    int c2 = 2;
    const int& constref2 = c2;

    // lvalue reference to const with an rvalue
    const int& r1 = 5;

    // lvalue reference to const with value of a different type
    char c = 'a';
    const int& r2 = c;

    printRef(r2); // 97

    return 0;
}