#include<bits/stdc++.h>
using namespace std;
 
 
int main()
{	

	int tam, aux, a, b=0;
	cin >> tam;
	auto numbers = vector<long long int> (tam);
	bool possible = true;
	for(auto &x: numbers){
		cin >> x;
	}
	// Find begin and end
	for(int i=0; i < tam -1; i++){
		if(numbers[i] > numbers[i+1]){
			a = i;
			break;
		}else{
			a = -1;
		}
	}
	// end
	b = a + 1;
	for(int i= a+1; i < tam -1; i++){
		if(numbers[i] > numbers[i+1])
			b = i+1;
	}

	if(a == tam - 2){
		b = tam -1;
	}
	// change
	int aux_a = a; 
	int aux_b= b;

	if(a == -1){
		a = b =0;
	}else{
		int changes = abs(a-b);
		// REVERSING
		if(changes == 1){
			aux = numbers[aux_a];
			numbers[aux_a]= numbers[aux_b];
			numbers[aux_b] = aux;
			aux_a++;
			aux_b--;
		} else{

			if(changes%2 == 1){
				changes--;
			}
			while(changes!=1){

				changes --;
				aux = numbers[aux_a];
				numbers[aux_a]= numbers[aux_b];
				numbers[aux_b] = aux;
				aux_a++;
				aux_b--;
			}

		}
	}
	for(auto x : numbers){
		cout << x << " " << endl;
	}

	//test
	for(int i=0; i < tam - 1; i++){
		if(numbers[i] > numbers[i+1]){
			possible = false;
			break;
		}
	}

	if(possible){
		cout << "yes" << "\n";
		cout << a+1 << " " << b+1;
	}else{
		cout << "no" << "\n";
	}

	return 0;
}