#include <iostream>

void swap(int a, int b){
    int temp = a;
    a = b;
    b = temp;
}

int main(){
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

    return 0;
}