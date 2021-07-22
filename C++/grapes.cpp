// Question link: https://codeforces.com/problemset/problem/1114/A
#include <bits/stdc++.h>
using namespace std;

int main() {
    int x,y,z,a,b,c;
    cin >> x >> y >> z;
    cin >> a >> b >> c;
    int flag = 0;

    if(x > a) {
        flag += 1;
    }

    if(y > (a+b-x)) {
        flag += 1;
    }

    if(z > (a+b+c-y-x)) {
        flag += 1;
    }

    if(flag > 0) {
        cout << "NO";
    } else {
        cout << "YES";
    }

    return 0;
}