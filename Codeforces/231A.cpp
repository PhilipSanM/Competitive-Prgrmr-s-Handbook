#include <bits/stdc++.h>
using namespace std;

int main(){
	int number_problems, solve = 0;
	int bit, flag = 0;
	cin >> number_problems;
	for(int i=0; i < number_problems; i++){
		for(int j=0; j<3 ; j++){
			cin >> bit;
			if (bit == 1){
				flag++;
			}
		}
		if (flag >= 2)
		{
			solve++;
		}
		flag=0;
	}
	cout << solve << endl;

	return 0;
}