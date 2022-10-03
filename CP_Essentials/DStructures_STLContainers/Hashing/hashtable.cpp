#include <iostream>
#include <unordered_map>
#include<map>
using namespace std;

int main(){

    // Key -> Value

    unordered_map<string,int> menu; // keys and values
    // map<string,int> manu; This is a O(logn) Operation with map
                        // becuase its a tree
                        // And this is sorting with the alphav=betic only keys


    // Insert Key Value pairs inside the hashtable  O(1) operation
    menu["maggi"] = 15;
    menu["colddrink"] = 20;
    menu["dosa"] = 99;


    // Update query
    menu["dosa"] = (1 + 0.1)*menu["dosa"];


    // Deletion
    menu.erase("maggi");

    //Searching in a collection
    string item;
    cin >> item;

    if(menu.count(item) == 0){
        cout << item << " is not available"<< endl;
    }else{
        cout << item << " is available, and its cost is: " << menu[item] << endl;
    }

    // We can iterate over all the key-values pair that are present
    for(pair<string,int> item : menu){
        cout << item.first << " - " << item.second << endl;
    }

    return 0;
}