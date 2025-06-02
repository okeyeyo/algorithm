#include<iostream>
#include<vector>
// #include <stdio.h>

using namespace std;

int isHour(int hour) {
	if(hour > 23) {
		return hour % 24;
	} else return hour;
}

int main() {
	int A, B, C, fin_h, fin_m;

	cin >> A >> B;
	cin >> C;

	if(B+C > 59) {
		fin_m = (B+C) % 60;
		fin_h = A + (B+C) / 60;
		cout << isHour(fin_h) << " " << fin_m;
	} else {
		fin_m = B+C;
		cout << A << " " << fin_m;
	}

	return 0;
}