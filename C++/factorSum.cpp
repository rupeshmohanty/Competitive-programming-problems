// Question Link: https://www.geeksforgeeks.org/sum-factors-number/#
#include <bits/stdc++.h>
using namespace std;

int sum(int num) {
    int s = 0;
    if(num == 1) {
        return 1;
    }

    for(int i = 2;i <= sqrt(num);i++) {
        if(num % i == 0) {
            if(i == (num/i)) {
                s += i;
            } else {
                s += i+(num/i);
            }
        }
    }

    return (s+num+1);
}

int main() {
    int n;
    cin >> n;
    int res = 0;

    res = sum(n);
    cout << res;
    return 0;
}