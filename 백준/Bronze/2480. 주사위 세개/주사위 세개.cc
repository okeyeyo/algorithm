#include <iostream>

int findBiggest(int a, int b, int c) {
	if(a>b && a>c)	return a;
		else if(b>a && b>c)	return b;
			else if(c>a && c>b)	return c;
}

int findSame(int a, int b, int c) {
	if(a==b && a!=c || a==c && a!=b) return a;
		else if(b==c || b!=a) return b;
}

using namespace std;

int main() {
	int A, B, C, big, same;

	cin >> A >> B >> C;

	if(A==B && A==C && B==C) {
		cout << 10000+A*1000;
	}	else if(A!=B && A!=C && B!=C) {
		big = findBiggest(A,B,C);
		cout << big*100;
	}	else {
		same = findSame(A,B,C);
		cout << 1000+same*100;
	}

	return 0;
}