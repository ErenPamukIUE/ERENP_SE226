//
// Created by erenp on 27.02.2026.
//
#include <iostream>
#include <string>
using namespace std;
int main() {
    int time;
    cin >> time;
    int firstTime = time;
    int hours = time / 3600;
    time = time % 3600;
    int minutes = time / 60;
    time = time % 60;
    int seconds = time;

    cout<<firstTime<<" Seconds is "<<hours
    << " Hours, " << minutes << " Minutes, and " << seconds<<" Seconds " <<endl;



    return 0;
}