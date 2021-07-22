// Question Link: https://www.geeksforgeeks.org/sieve-of-eratosthenes/
#include <bits/stdc++.h>
using namespace std;

bool checkPrime(int num) {
    bool flag = false;
    for(int i = 2;i < num;i++) {
        if(num % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int n;
    bool res = false;
    cin >> n;

    for(int i = 2;i < n;i++) {
        res = checkPrime(i);

        if(res) {
            cout << i << " ";
        }
    }   
    return 0;
}