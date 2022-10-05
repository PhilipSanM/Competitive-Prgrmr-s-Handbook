#include<bits/stdc++.h>
using namespace std;


int main()
{	
	int cases, a,b,c,n;
	cin >> cases;
	while( cases --){
		cin >> a >> b >> c >> n;
		while( a != b && b!= c){
			// The max value
			int max;
			int difference =0;
			if(a > b and a > c){
				max = a;
			}else if(b > a and b > c){
				max = b;
			}else if(a == b and b== c){
				if(n%3 == 0){
					cout << "YES" << "\n";
					break;
				}else{
					cout << "NO" << "\n";
					break;
				}
			}else max = c;

			// working with the max value
			difference = abs(max - a);
			a += difference; //same value with a = max
			n -=difference;
			difference = abs(max - b);
			b += difference; //same value with a = max
			n -=difference;
			difference = abs(max - c);
			c += difference; //same value with a = max
			n -=difference;
			if(n < 0 ){
				cout << "NO" << "\n";
				break;
			}else if(n%3 == 0){
				cout << "YES" << "\n";
				break;
			}else{
				cout << "NO" << "\n";
				break;
			}

		}
		
	}
	return 0;
}