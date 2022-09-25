# Language Features

A typical C++ code template for competitive programming look like this:
```CPP
#include<bits/stdc++.h>

using namespace std;

int main(){
  // solution comes here
}
```

And the code can be compiled using the following command:
```
g++ -stc=c++11 -O2 -Wall test.cpp -o test
```

The compiler follows the C++ 11 standard (-std=c++11), optimizes the code (-O2), and shows warnings about possible errors (-Wall)
