#include<bits/stdc++.h>
using namespace std;

bool detectCapitalUse(string word) {
	auto num_capitals = count_if(word.begin(),word.end(),
		[]( char c ){ return isupper(c); } );

	if (num_capitals == 0 )return true;else if(num_capitals == 1 && isupper(word[0]))return true; else if(num_capitals == (int)word.size()) return true; else return false;
	
	
}

int main()
{	
	string s;
	cin >> s;
	cout << detectCapitalUse(s);
	return 0;
}