/****
 * 
 *  deque
 * 
 */
// Doble-ended queue is sequence containers with dynamic sizes that can be
// expanded or contracted on both ends (front or back)

// METHODS

// pop_back()
// pop_front()
#include<bits/stdc++.h>
using namespace std;

deque<int> first;           // Empty deque of ints
deque<int> second (4,100);  // four ints with value 100
deque<int> third (second.begin(),second.end()); // iterating through second
deque<int> fourth (third);  // a copy of third

// The iterator constructor can be used to copy arrays:
int myints[] = {16,2,77,29};
int n = sizeof(myints)/sizeof(int);

deque<int> fifth (myints,myints+n);


deque<int> dq = {23,45,12};
// // push_back
// dq.push_back(8);

// dq.push_front(14);

// dq.pop_back();

// dq.pop_front();


int main(){
    deque<int> dq(10);
    for(int i=0; i<dq.size(); i++){
        dq[i] = i*i;
    }

    cout << "\n Size ";
    cout << dq.size() << endl;

    for(int x:dq){
        cout << x << ", ";
    }

    return 0;
}