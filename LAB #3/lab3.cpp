#include <iostream>
using namespace std;
// TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.


void swapValues(int* p1 , int* p2) {
    int temp = *p2;
    *p2 = *p1;
    *p1 = temp;

}
void reverseArray(int* arr , int size) {
    int left = 0;
    int right = size - 1;

    while(left < right) {
        swapValues( (arr + left) , (arr + right));
        left++;
        right--;
    }
}
void printArray(int* arr , int size) {
    for (int i = 0 ; i< size ; i++) {
        cout<<*arr<<" ";
        arr++;
    }
}

int findMax(int* arr , int size) {
    int max = arr[0];
    for (int i = 0  ; i< size ; i++) {
        if(  *(arr + i) > max  ) {
            max = *(arr+i);
        }
    }

    return max;
}
int* createArray(int size) {
    int *arr;
    arr = new int[size];
    return arr;
}

void deleteArray(int* arr) {
    delete[] arr;
    arr = nullptr;
}


int main() {
cout<<"Creating dynamic array... "<<endl;
    cout<<"Enter array size : ";
    int size;
    cin>>size;
    int *arr;
    arr = new int[size];
    cout<<"\nEnter Values : ";
    for (int i = 0 ; i<size ; i++) {
        cin>> *(arr + i);
    }

    cout<<"\nArray Elements : \n";
    printArray(arr,size);

    cout<< "\nMaximum Element : "<< findMax(arr,size);
    cout<<"-----------------------------------------"<<endl;
    cout<<"Swapping Two Numbers"<<endl;

    int a = 8;
    int b = 5;
    cout<<"Before Swap:\na = "<<a<<"\nb = "<<b<<endl;
    swapValues(&a,&b);
    cout<<"After Swap:\na = "<<a<<"\nb = "<<b<<endl;
    cout<<"-----------------------------------------\nReversing array...\n\nArray after reverseArray: \n";
    reverseArray(arr,5);
    printArray(arr,5);
    cout<<"\n-----------------------------------------\nDeleting array..."<<endl;
    deleteArray(arr);
    cout<<"Memory released successfully";







    return 0;
}

