#include <iostream>

// Function templates let us declare functions without specifying the data type
// Accepting two data types
// The auto keyword allows the function to decide what datatype to return
template<typename T, typename U>
auto max(T x, U y){
    return (x > y) ? x : y;
}

int main(){
    std::cout << max("1", "2") << std::endl;
    std::cout << max(2,4) << std::endl;
    std::cout << max(0.5, 2.1) << std::endl;
    return 0;
}