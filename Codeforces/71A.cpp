#include <bits/stdc++.h>
using namespace std;

int main(){

	int number_words;
	string word;
	cin >> number_words;
	for(int i = 0; i < number_words; i++){
		cin >> word;
		if(word.size() > 10){ // bytes
			cout << word.front() << word.length() -2 << word.back() << "\n";
		}else{
			cout << word << endl;
		}		
	}

	return 0;
}