/* 
Reference: 
https://www.programiz.com/cpp-programming/type-conversion-operators

Four type conversion operators:
1. static_cast: standard type conversion
2. dynamic_cast: polymorphic type conversion
3. const_cast: cast away the const qualifier from a variable to allow modification
4. reinterpret_cast: convert one pointer type to another pointer type or one reference type to another reference type (usually low level use)
*/

#include <iostream>
using namespace std;

class Base {
public:
    // base class print function
    virtual void print(){
        cout << "Base class" << endl;
    }
};

class Derived : public Base {
public:
    // derived class print function overriding the base class
    void print() override{
        cout << "Derived class" << endl;
    }
};

// function that takes a non-const pointer
void modify_data(int* data){
    *data *= 2;
}

int main(){
    // static_cast 
    float my_float = 3.14;
    int my_int = static_cast<int>(my_float); // float -> int
    cout << "Float: " << my_float << " -> Int: " << my_int << endl;

    /*
    dynamic_cast for polymorphic type conversions, especially when dealing with inheritance hierachies;
    typically used in scenarios where a base class pointer needs to be converted to a derived class pointer
    */
    // pointing to a derived object
    Base *base_ptr = new Derived();

    // use dynamic_cast to cast the base pointer to a derived pointer
    Derived *derived_ptr = dynamic_cast<Derived*>(base_ptr);

    // call the print function through the derived pointer
    if (derived_ptr){
        derived_ptr->print();
    }

    delete base_ptr;

    // const_cast
    int x = 10;
    // a const pointer for variable x
    const int* ptr = &x;
    int* mutable_ptr = const_cast<int*>(ptr);
    modify_data(mutable_ptr);
    cout << "Modified value: " << x << endl;

    // reinterpret_cast: doesn't actually convert the data types but reinterprets one pointer type as another at compile time
    int y = 67;

    int *ptr_to_int = &y; // ASCII 67: C

    char *ptr_to_char = reinterpret_cast<char*>(ptr_to_int);

    cout << "Dereferencing ptr_to_char: " << *ptr_to_char << endl;
    return 0;
}