#include <iostream>
#include "io.h"

using namespace std;

int readNumber(){
    int x{};
    cout << "Enter a number: ";
    cin >> x;
    return x;
}

void writeAnswer(int x){
    cout << "The answer is " << x << std::endl;
} 