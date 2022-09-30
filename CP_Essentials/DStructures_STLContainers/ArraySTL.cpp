#include <iostream>
#include <array>
#include <algorithm>
using namespace std;

/****
 *  ALL STL CONTAINERS ARE PASSED BY VALUE
 * ***/


// Update an array
// PASSED BY VALUE
void updateArray(array<int,9> arr, int i, int val){
    arr[i] = val;
}
// By reference
void updateArrayB(array<int,9> &xarr, int i, int val){
    xarr[i] = val;
}

//print
// void print(array<int,6> arr){
//     for(int i = 0; i < arr.size(); i++){
//         cout << arr[i]<< " ";
//     }
//     cout << endl;
// }

// Also you can do this for just a read function:
void print(const array<int,9> &arr){
    // arr[0] = 100;
    for(int i = 0; i < arr.size(); i++){
        cout << arr[i]<< " ";
    }
    cout << endl;
}


int main(){
    array<int, 9> arr = {1,2,36,6,7,8,100,45,4};

    // arr[0] = 10;
    updateArray(arr,0,10); // The array is not updated
    updateArrayB(arr,1,10); // The array is not updated

    //PRINT
    print(arr);

    // sort
    sort(arr.begin(), arr.end());
    print(arr);

    //fill
    array<int,10> fives;
    fives.fill(5);
    for(int i =0; i< fives.size();i++){
        cout << fives[i] << " ";
    }
    cout << endl;

    // For Each Loop
    for(int x: fives){
        cout << x << " ";
    }
    cout << endl;
    return (0);
}

// array.at(i) Get ith element
// array.back() Get the last element
// array.front()
// 