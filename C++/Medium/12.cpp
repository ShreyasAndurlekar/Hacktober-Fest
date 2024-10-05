#include <iostream>
using namespace std;
int area(int radius)
{
    const double PI = 3.14; // should be double not string
    return PI * radius * radius;
}
int main()
{
    int radius = 10;
    cout << area(radius) << endl;
}
