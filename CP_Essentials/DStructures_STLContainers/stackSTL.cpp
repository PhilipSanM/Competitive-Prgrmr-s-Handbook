#include<bits/stdc++.h>
// #include<stack>
using namespace std;

int main(){

    stack<string> books;
    
    books.push("C++");
    books.push("Java");
    books.push("Linux");

    while(!books.empty()){
        cout << books.top() << endl;
        books.pop();
    }

    return 0;
}