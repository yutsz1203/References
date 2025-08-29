#include <iostream>
// function pointer points to the address of the first line of the code of the corresponding function
// return_type (*pointer_name)(data_typ1, data_type2,...);
// invoking a function pointer: (*fun_ptr)(arg1, arg2)
// references to function: func_type func(return_type_of_function_pointer(&pointer_name)(data_type1, data_type2))

int add(int a, int b){
    return a + b;
}

void fun_1(){
    std::cout << "Function - 1 is called." << std::endl;
    return;
}

// a callback function
void fun_2(void (*ptr)()){
    (*ptr) ();
    std::cout << "Function - 2 is called." << std::endl;
}

// Function Pointer as Return Type
// define the function pointer type
typedef int (*ptr)(int);
typedef ptr (*pointer)();

int returnAdd(int x){
    std::cout << "from the add function!" << std::endl;
    return x + 5;
}

// function that returns a function pointer
ptr print(){
    std::cout << "The sum is ";
    return &returnAdd;
}

// References To Functions
int func_1(){
    std::cout << "Function - 1 is called." << std::endl;
    return 5;
}

// function that takes reference as an argument
int func_0(int(&F)()){
    std::cout << "Function - 0 is called." << std::endl;
    return F();
}

int main(){
    int (*funcptr) (int, int) = add;
    int sum = funcptr(4,5);
    std::cout << sum << "\n";

    // callback functions
    void (*ptr)() = &fun_1;
    fun_2(ptr);

    // address of a function
    // both with or without the "&" will get the address
    std::cout << "Address of the main() function is : " << reinterpret_cast<void*>(main) << std::endl;
    std::cout << "Address of the add() function is : " << reinterpret_cast<void*>(&add) << std::endl;

    // function pointer as return type
    int x = 45;
    pointer n = print;
    std::cout << (*n())(x) << std::endl;

    // References to functions
    int y = func_0(func_1);
    std::cout << "The value of y is: " << y << std::endl;
    return 0;
}