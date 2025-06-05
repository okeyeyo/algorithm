#include <iostream>

using namespace std;

int main() {
	int N, a, b;
	long long X, total = 0;

	cin >> X;
	cin >> N;

	for(int i = 0; i<N; i++) {
		cin >> a >> b;
		total += a*b;
	}

	if(X == total) cout << "Yes";
	 else cout << "No";

	return 0;
}