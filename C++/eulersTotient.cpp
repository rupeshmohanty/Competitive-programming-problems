// Question Link: https://www.geeksforgeeks.org/eulers-totient-function/
#include <bits/stdc++.h>
using namespace std;
int findGcd(int a,int N) {
    if(a == 0) {
        return N;
    }

    return findGcd(N % a,a);
}

int eulerGcd(int num) {
    int count = 0;
    int r = 0;

    if(num == 1) {
        return num;
    } else {
        for(int i = 1;i <= num;i++) {
            r = findGcd(i,num);
            if(r == 1) {
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

    res = eulerGcd(n);

    cout << res;
    return 0;
}