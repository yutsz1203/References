// dataType *pointerName;
#include <iostream>

int main(){
    // Pointers
    int num = 10;
    int *ptr = &num;

    // dereferencing
    int value = *ptr;
    std::cout << value << "\n";

    // References
    // dataType &referenceName = existingVariable;
    // Modifying the value of ref will also modify the value of num
    // Used when pass variable by reference in function arguments
    int num2 = 10;
    int &ref = num;

    std::cout << ref << "\n";
    return 0;
}