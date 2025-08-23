#include <string>
#include <iostream>
// Structures (stuct)
// used to store different data types under a single variable and accessibility of member variables and methods are public

struct Person{
    std::string name;
    int age;
    float height;
};

Person p1 = {"John Doe", 30, 5.9};

// Classes (class)
// Similar to structures, but accessibility of the member data and function are governed by access specifiers (public / private)

class Guy{
public:
    std::string name;
    int age;

    void printInfo(){
        std::cout << "Name: " << name << ", Age: " << age << "\n";
    };
};

// Unions (union)
// used to store different data types in the same memory location
union Data {
    int num;
    char letter;
    float decimal;
};

int main(){
    Guy g1; 
    g1.name = "John Doe";
    g1.age = 30;

    Data mydata;
    mydata.num = 42;
    return 0;
}