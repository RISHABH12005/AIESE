#include <iostream>
using namespace std;
int add(int a, int b)
{
	return a+b;
}
int subtract(int a, int b)
{
	return a-b;
}
int multiply(int a, int b)
{
	return a*b;
}
double divide(int a, int b)
{
	if (b == 0)
		return 0;
	return static_cast<double>(a) / b;
}
int main()
{
	int x, y;
	cout << "Enter 2 No.";
	cin >> x >> y;
	cout << "Sum =" << add(x,y) << endl;
	cout << "Difference =" << subtract(x,y) << endl;
	cout << "Product =" << multiply(x,y) << endl;
	if (y != 0)
		cout << "Quotient =" << divide(x,y) << endl;
	else
		cout << "Cannot divide by zero" << endl;
	return 0; 
}