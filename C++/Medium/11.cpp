#include <iostream>
using namespace std;
int main()
{
    int a = 5, b = 10;
    if ((a > 0 || b < 5) && a < 10) // brackets should be properly structured
    {
        cout << "Condition met" << endl;
    }
    return 0;
}
