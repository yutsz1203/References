#include <iostream>

void swap(int a, int b){
    int temp = a;
    a = b;
    b = temp;
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
    const int& ref = 5;

    // lvalue reference to const with value of a different type
    char c = 'a';
    const int& r2 = c; // 97

    return 0;
}