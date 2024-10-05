#include <iostream>
using namespace std;
void print(int a)
{
    cout << "Integer: " << a << endl;
}
void print(float a)
{
    cout << "Float: " << a << endl;
}
int main()
{
    print(static_cast<float>(5.0)); // any decimal numbers are regarded as doubles in C++ not float so we need to epllicity state it's a float so it can find proper function
    return 0;
}
