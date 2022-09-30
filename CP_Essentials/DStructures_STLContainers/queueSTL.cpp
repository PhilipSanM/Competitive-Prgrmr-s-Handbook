#include<bits/stdc++.h>

using namespace std;

class Compare{
public:
    bool operator()(int a, int b){
        return a > b; // <
    }
};

int main(){
    queue<int> q;

    q.push(1);
    q.push(10);
    q.push(45);
    
    while(!q.empty()){
        cout << q.front() << endl;
        q.pop();
    }
    cout << "-----------------" << endl;
    // PRIORITY QUEUE
    int arr[] = {10,23,12,43,12,5};
    int n = sizeof(arr)/sizeof(int);

    priority_queue<int> heap; // Max HEAP

    for( int x: arr){
        heap.push(x);
    }

    while(!heap.empty()){
        cout << heap.top()<< endl;
        heap.pop();
    } // 43 23 12 12 10 5

    cout << "-----------------" << endl;
    // priority_queue<int, vector<int>, greater<int>> heapMin;
    priority_queue<int, vector<int>, Compare> heapMin;
    for( int x: arr){
        heapMin.push(x);
    }

    while(!heapMin.empty()){
        cout << heapMin.top()<< endl;
        heapMin.pop();
    } // 43 23 12 12 10 5

    return 0;
}