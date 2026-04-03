#include <iostream>
#include <cmath>
using namespace std;
int i = 0;
int summation = 0;


void powerSum(int n, int r) {
    if (n < 1) {
        return;
    }
    if(i > n) {
        return;
    }

        summation += std::pow(r,i);
        i++;
        powerSum(n,r);
}

int main() {
    powerSum(3,1);
    cout<<summation<<endl;


    return 0;
}