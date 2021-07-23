// Question Link: https://www.geeksforgeeks.org/eulers-totient-function-for-all-numbers-smaller-than-or-equal-to-n/
#include <bits/stdc++.h>
using namespace std;

int gcd(int a,int N) {
    if(a == 0) {
        return N;
    }

    return gcd(N%a,a);
}

int eulerGcd(int n) {
    int count = 0;
    if(n == 1) {
        return 1;
    } else {
        for(int i = 1;i <= n;i++) {
            if(gcd(i,n) == 1) {
                count++;
            }
        }
    }

    return count;
}


int main() {
    int n;
    cin >> n;
    int res = 0;

    for(int i = 1;i <= n;i++) {
        res = eulerGcd(i);
        cout << "Totient of " << i << " is " << res << endl;
    }

    return 0;
}