// Question Link: https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,m;
    cin >> n >> m;
    int gcd = 1;

    if(m % n == 0) {
        gcd = n;
    } else {
        for(int i = 2;i <= min(m,n);i++) {
            if(m % i == 0 && n % i == 0) {
                if(i > gcd) {
                    gcd = i;
                }
            }
        } 
    }

    cout << (n*m)/gcd;
    return 0;
}