// Question Link: https://www.geeksforgeeks.org/write-an-iterative-olog-y-function-for-powx-y/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int x,y;
    cin >> x >> y;
    int res = 1;

    while(y > 0) {
        res = res*x;
        y--;
    }

    cout << res;
    return 0;
}