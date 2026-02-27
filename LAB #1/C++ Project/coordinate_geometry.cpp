//
// Created by erenp on 27.02.2026.
//
#include <iostream>
#include <cmath>
#include <string>
using namespace std;
int main() {
    int X1;
    int Y1;
    int X2;
    int Y2;
    cout<<"X1:";
    cin>>X1;
    cout<<"Y1:";
    cin>>Y1;
    cout<<"X2:";
    cin>>X2;
    cout<<"Y2:";
    cin>>Y2;

    float distance = sqrt(pow(X2-X1,2)+pow(Y2-Y1,2));

    cout<<"Distance is "<<distance<<endl;

    return 0;
}