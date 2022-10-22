#include<bits/stdc++.h>
using namespace std;
 
 
int main()
{	
	int cases;
	cin >> cases;
	while( cases --){
		int a,b,c,n;
		cin >> a >> b >> c >> n;
		auto max_money = max({a,b,c});
		int money_to_give = (max_money - a) + (max_money - b) + (max_money -c);
		int left =  n - money_to_give;
		if(left<0){
			cout << "NO" << "\n";
		}else{		(left%3 == 0 or left == 0) ? cout << "YES" << "\n" : cout << "NO" << "\n";}
		
	}
	return 0;
}