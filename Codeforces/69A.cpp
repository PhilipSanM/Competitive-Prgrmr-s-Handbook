#include<bits/stdc++.h>
#define endl '\n'

using namespace std;

int main()
{	
	int n,x =0,y =0,z=0, vx =0,vy=0,vz=0;
	cin >> n;
	while(n--){
		cin >> vx >> vy >> vz;
		x += vx;
		y += vy;
		z += vz;
	}
	( x == 0 and y == 0 and z== 0) ? cout << "YES": cout << "NO";
	return 0;
}