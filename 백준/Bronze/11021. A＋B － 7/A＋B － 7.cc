#include <iostream>

using namespace std;

int main() {

	int T, a, b;

	cin >> T;
	int sum[T];

	for(int i=0; i<T; i++) {
		cin >> a >> b;
		sum[i] = a+b;
	}

	for(int i=0; i<T; i++) {
		cout << "Case #" << i+1 << ": " << sum[i] << "\n";
	}

	return 0;
}