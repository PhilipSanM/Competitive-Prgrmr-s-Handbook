#include <iostream>
#include<unordered_set>
using namespace std;

int main(){

    // set is just a collection of keys
    // each insertions is 0(1)
    unordered_set<int> s{1,2,3,4,78,32,2,1};

    int key;
    cin >> key;
    //s.end() Its a direction after the last element
    if(s.find(key)!=s.end()){ //O(1)
        cout << key << " is present\n";

    }else{
        cout << "Not found"<<endl;
    }
    s.insert(111);
    s.erase(3);

    // let us print all the elements in the set
    for(int x: s){
        cout << x << endl;
    }



    return 0;
}