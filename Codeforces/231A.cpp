#include<bits/stdc++.h>
using namespace std;


int main(){	
	long long int a,b,n;
	cin >> a >> b >> n;
	while(n--){
		// 1 - 9
		a *= 10;
		long long int  test_number;
		bool possible= false;		
		for(int i = 0; i <= 9; i++){
			test_number = a + i;
			if(test_number%b == 0){
				possible = true;
				break;
			}
		}
		if(possible){
			a = test_number;
		}else break;
	}
	if(n == -1){
		cout << a;
	}else{
		cout << -1;
	}

	return 0;
}