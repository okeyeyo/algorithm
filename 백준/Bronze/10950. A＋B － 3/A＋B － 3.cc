#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T, n1, n2;

	cin >> T;
	vector<int> sum(T);

	for(int i = 0; i<T; i++) {
		cin >> n1 >> n2;
		sum[i] = n1+n2;
	}

	for(int i = 0; i<T; i++) {
		cout << sum[i] << endl;
	}

	return 0;
}