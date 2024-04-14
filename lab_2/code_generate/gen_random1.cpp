#include <iostream>
#include <random>
#include <ctime>
#include <fstream>
#include <vector>

using namespace std;

void generate(vector<int>& list) {
	srand(time(NULL));
	for (auto& el : list) {
		el = (rand() % 2);
	}
}

int main() {
	vector<int> list(128);
	generate(list);
	ofstream file("C:\\Users\\natal\\isb_lab1\\lab_2\\generate\\gen_int_c++.txt");
	for (auto& el : list) {
		file << el;
	}
	file.close();
	return 0;
}