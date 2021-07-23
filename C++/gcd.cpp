// Question Link: https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/
#include <bits/stdc++.h>
using namespace std;

int gcd(int num1,int num2) {
    if(num1 > num2) {
        if(num1 % num2 == 0) {
            return num2;
        } 

        return gcd(num1-num2,num2);
    } else {
        if(num2 % num1 == 0) {
            return num1;
        }

        return gcd(num1,num2-num1);
    }
}

int main() {
    int n,m;
    cin >> n >> m;
    int res = 0;

    res = gcd(n,m);
    cout << res;
    return 0;
}