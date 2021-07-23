// Question Link: https://www.geeksforgeeks.org/linear-diophantine-equations/
#include <bits/stdc++.h>
using namespace std;

int gcd(int a,int b) {
    if(a > b) {
        if(a % b == 0) {
            return b;
        }

        return gcd(a-b,b);
    } else {
        if(b % a == 0) {
            return a;
        }

        return gcd(a,b-a);
    }
}

int main() {
    int a,b,c;
    int res = 0;

    cin >> a >> b >> c;

    res = gcd(a,b);
    if(c % res == 0) {
        cout << "Possible";
    } else {
        cout << "Not possible";
    }
}