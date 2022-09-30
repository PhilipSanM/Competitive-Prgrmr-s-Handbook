#include <iostream>
#include <algorithm>

using namespace std;

// Array to functions.
// Array is passed by reference
void updateArray(int arr[],int i, int val){
    arr[i] = val;
}


void print(int arr[], int n){
    for(int i=0; i<n; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

void arratSize(int arr[]){
    cout << "Array Size in Function: " << sizeof(arr); //8 -> sizeof int *
    cout << endl;
}

int main(){
    int arr[5] = {1,5,4,3,2};
    int n = sizeof(arr)/sizeof(int); // 20 bytes / 4 bytes = 5
    
    // When you use a function of an array youare passing the pointer
    // the direction of the beginning fo that arrat
    cout << "Array Size in Main: " << sizeof(arr); // 20
    cout << endl;
    arratSize(arr);

    // Actual array is updated
    updateArray(arr,3,13);

    //print 
    print(arr, n);

    // sort
    sort(arr, arr + n);
    print(arr,n);

    return 0;
}