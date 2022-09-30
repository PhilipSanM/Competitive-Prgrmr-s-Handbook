/****
 * 
 *  V E C T O R S
 * 
 */
// Dynamic array wiith the ability to resize itself automaticallly when
// an element is inserted


// METHODS:
// []
// at()
// back()
// begin()
// clear()
// pop_back()
// push_back()
// reserve()
// clear()
// size()

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// // Empty container constructor
// vector<int> first;
// // Fill constructor (4 intergers with valuee 20)
// vector<int> second(4,20);

// // Range constructor
// int numbers[] = {10,20,30,40};
// vector<int> third(numbers,numbers+4);

// // Copy Constructor
// vector<int> four(third);

// // another way
// vector<int> fifth = {10,230,201,12};

int main(){
    vector<int> v;
    int n;
    cin >> n;

    for(int i=0; i<n; i++){
        int no;
        cin >> no;
        v.push_back(no);
        cout << "Capacity: "<< v.capacity() << "  Size: " << v.size() << endl;  
    } // cAPACITY means 1, 2, 4, 8, 16, 31 ...
    // v.reserve(100);// You reserve 100 elements of capacity in the vector

    // sorting
    sort(v.begin(),v.end());

    for(int x: v) cout << x << " ";


    return 0;
}