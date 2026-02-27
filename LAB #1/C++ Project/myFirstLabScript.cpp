//
// Created by erenp on 27.02.2026.
//
#include <iostream>
#include <string>
using namespace std;


int main() {
    string name;
    std::cout << "What is your name?\n";
    cin >> name;
    cout<<"Hello " << name<<"\nWhat is your Student ID?\n";
    int studentID;
    cin >> studentID;
    cout <<"Your ID is "<<studentID<<endl;

    return 0;
}