// Question Link: https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int x,y,p;
    cin >> x >> y >> p;
    int res = 1;

    while(y > 0) {
        res = res*x;
        y--;
    }

    cout << res%p;

    return 0;
}