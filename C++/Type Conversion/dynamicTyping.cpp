/*
Dynamic Typing refers to determining the data types of variables at runtime, instead of compiled time
*/
#include<iostream>
#include<any>

int main(){
    // void* pointer is a generic pointer that can point to objects of any data type
    int x = 42;
    float y = 3.14f;
    std::string z = "Hello, world!";

    void* void_ptr;

    void_ptr = &x;
    std::cout << "int value: " << *(static_cast<int*>(void_ptr)) << "\n";

    void_ptr = &y;
    std::cout << "float value: " << *(static_cast<float*>(void_ptr)) << "\n";

    void_ptr = &z;
    std::cout << "string value: " << *(static_cast<std::string*>(void_ptr)) << "\n";

    // std::any (C++17), a generalised type-safe container for single values of any type
    std::any any_value;

    any_value = 42;
    std::cout << "int value: " << std::any_cast<int>(any_value) << "\n";

    any_value = 3.14;
    std::cout << "double value: " << std::any_cast<double>(any_value) << "\n";

    any_value = std::string("Hello, world!");
    std::cout << "string value: " << std::any_cast<std::string>(any_value) << "\n";
    return 0;
}