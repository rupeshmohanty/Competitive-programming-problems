// Question Link: https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    for(int i = 1;i <= n;i++) {
        if(n % i == 0) {
            cout << i << " ";
        }
    }
    return 0;
}