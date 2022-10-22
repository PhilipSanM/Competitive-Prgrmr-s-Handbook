#include<bits/stdc++.h>
using namespace std;
// ====================================
// =============== Priority queue =====
// ====================================


// #include<queue>
 
int main(){
	priority_queue<int> pq;
	int snume;
	cin >> snume;
	cout << snume << endl;
	pq.push(2);
	pq.push(5);


	cout << "\n\n";
	while(!pq.empty()){
		cout << "----" << pq.top() << "\n";
		pq.pop();
	}
	return 0;
}