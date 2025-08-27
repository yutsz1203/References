// Run-time type identification (RTTI)
// using typeid to get the type of an object
#include <iostream>
#include <typeinfo>

class Base { virtual void dummy() {}};
class Derived : public Base { };

int main(){
    Base* base_ptr = new Derived;

    std::cout << "Type: " << typeid(*base_ptr).name() << std::endl;
    std::cout << "Int type: " << typeid(1).name() << std::endl; // i
    std::cout << "Float type: " << typeid(1.0f).name() << std::endl; // f
    std::cout << "Double type: " << typeid(1.0).name() << std::endl; // d
    std::cout << "Char type: " << typeid('a').name() << std::endl; // c

    delete base_ptr;
    return 0;
}