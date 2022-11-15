#include<iostream>
#include<string.h>
#include<cstdlib>
using namespace std;
int t, p;
string keyboard, query;

int search(string keyboard, char letter) {
	for (int i = 0; i < sizeof(keyboard); i++) {
		if (keyboard[i] == letter) {
			return i;
		}
	}
	return 0;
}
int main() {
	cin >> t;
	int te = t*2;
	while (te--) {
		cin >> keyboard;
		cin >> query;
		p = 0;
		for (int i = 0; i < sizeof(query); i++) {
			if ((i+1) < sizeof(query)) {
				p += abs(search(keyboard, query[i]) - search(keyboard, query[i+1]));
			}
		}
		cout << p;
	}
}
