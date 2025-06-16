#include <iostream>

using namespace std;

int main() {
	int N,long_byte;

	cin >> N;

	long_byte = N/4;

	for(int i=0; i<long_byte; i++) {
		cout << "long" << " ";
	}

	cout << "int";

	return 0;
}