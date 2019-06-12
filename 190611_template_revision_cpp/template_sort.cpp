// Example program
#include <iostream>
#include <string>

struct Student {
	std::string name;
	int score;

	bool operator<(const Student &rhs) {
		return score < rhs.score;
	}

	// if it is swift, no need to overload "<<" operator...
	// just implement the customStringConvertible protocol.
	// TAT
};

template<typename T>
void selectionSort(T arr[], int n) {
	for (int i = 0; i < n; i++) {
		int minIndex = i;
		for (int j = i + 1; j < n; j++) {
			if (arr[j] < arr[minIndex]) {
				minIndex = j;
			}
		}
		std::swap(arr[i], arr[minIndex]);
	}
}

int main(int argc, char const *argv[]) {
	std::string c[4] = {"D", "C", "B", "A"};
	selectionSort(c, 4);
	for (int i = 0; i < 4; i++) {
		std::cout << c[i] << "";
	}
	std::cout << std::endl;
	return 0;
}