#include <iostream>
using namespace std;
void area(int radius)
{
    const double PI = 3.14;         // should not be string should be double
    return PI * radius * radius;
}
void main()
{
    int radius = 10;
    cout << area(radius) << endl;
}
