#include <iostream>

using namespace std;

int main() {

	int T;

	cin >> T;

	for(int i=1; i<=T; i++) {
		for(int j=0; j<i; j++) {
			cout << "*";
		}
		cout << "\n";
	}

	return 0;
}