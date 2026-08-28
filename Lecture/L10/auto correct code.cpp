#include <iostream>

int main()
{
	int firstNumber;
	int secondNumber;
	const int multiplier = 0;

	std::cin >> firstNumber >> secondNumber;
	const int sum = firstNumber + secondNumber;
	const int product = sum * multiplier;
	std::cout << product;

	return 0;
}