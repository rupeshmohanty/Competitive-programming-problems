// Question Link: https://www.hackerrank.com/challenges/extra-long-factorials/problem
#include <bits/stdc++.h>
using namespace std;

int extraLongFact(long long int num) {
    if(num == 1) {
        return 1;
    } else {
        return num * extraLongFact(num-1);
    }
}

int main() {
    long long int n;
    cin >> n;

    long long int res = 0;

    res = extraLongFact(n);
    cout << res;
}