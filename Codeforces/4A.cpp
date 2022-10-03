#include <bits/stdc++.h>
using namespace std;

int main(){

	int watermelon_weight;
	cin >> watermelon_weight;
	watermelon_weight %2 == 0 && watermelon_weight > 2? cout << "YES" : cout << "NO";
	return 0;
}