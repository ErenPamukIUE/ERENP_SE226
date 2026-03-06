//
// Created by erenp on 6.03.2026.
//
#include <iostream>
#include <string>
using namespace std;
int main() {


    //Task 1 Digital Root Sequence
    int value;
    int steps = 0;
    cout<<"Please enter a positive integer greater than 9:";

    cin >> value;

   while (value > 9) {
       cout<<value;
       int newVal = 0;
       while(value > 0) {
           newVal += value % 10;
           value /= 10;

       }
       value = newVal;
       steps++;
       cout<<"-->";
   }
    cout<<value<<endl;
    cout<<"Final Value : "<<value<<endl;
    cout<<"Total steps : " << steps<<endl;


    //Task 2 FizzBuzz Counter

    int fizz = 0;
    int buzz = 0;
    int fizzBuzz = 0;

    int value2;

        cout <<"Please enter a number between 10 and 100: "<<endl;
        cin >> value2;
    while (value2 < 10 || value2 > 101){
        cout<<"Invalid input. Please enter a number between 10 and 100: ";
        cin>>value2;
    }

    for (int i = 1 ; i <= value2 ; i++) {
        if (i % 7 == 0) {
            cout<<"("<<i<<" is skipped)"<<endl;
            continue;
        }


        if (i % 3 == 0 && i % 5 == 0) {
            cout<<"FizzBuzz"<<endl;
            fizzBuzz++;
        } else if (i % 3 == 0) {
            cout <<"Fizz"<<endl;
            fizz++;
        } else if (i % 5 == 0) {
            cout <<"Buzz"<<endl;
            buzz++;
        } else {
            cout<<i<<endl;
        }
    }

    cout <<"--Summary--\n"<<"Fizz count : "<<fizz
    <<"\nBuzz count : "<<buzz<<"\nFizzBuzz count : "<<fizzBuzz<<endl;


    //Task 3

    int count;


    cout <<"Please enter a number between 3 and 9: "<<endl;
    cin >> count;
    while (count < 3 || count > 9){
        cout<<"Invalid input. Please enter a number between 3 and 9: ";
        cin>>count;
    }

    for (int i=0; i<count ; i++) {
        for (int j=0; j<=i ; j++) {
            cout<<j +1;
        }
        cout<<endl;
    }
    for (int i=count -1 ; i>=1 ; i--) {
        for (int j=0; j<i ; j++) {
            cout<<j + 1 ;
        }
        cout<<endl;
    }








    return 0;
}