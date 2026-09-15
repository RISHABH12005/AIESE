#include <iostream>
using namespace std;
double calculateFine(int daysLate)
{
 if (daysLate < 0)
 return -1;
 return daysLate / 5;
}
int main()
{
 int daysLate;
 cout << "Enter number of days late: ";
 cin >> daysLate;
 double fine = calculateFine(daysLate);
 if (fine == -1)
 cout << "Invalid input";
 else
 cout << "Fine: " << fine;
 return 0;
}
