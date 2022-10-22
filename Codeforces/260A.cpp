#include<bits/stdc++.h>
using namespace std;


int main(){	
	long long int a,b,n;
	bool possible = false;
	cin >> a >> b >> n;
	for(int i = 0;  i <= 9; i++){
		if((a*10 + i)%b == 0){
			cout << a*10 + i;
			string s(n-1, '0');
			cout << s << "\n";
			possible = true;
			break;
		}

	}
	if(!possible){
		cout << -1 << "\n";
	}
	return 0;
}