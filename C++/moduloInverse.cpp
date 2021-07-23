// Question Link: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,m;
    cin >> a >> m;
    int x = 0;

    int i = 1; 
    while(i < m){
        if((a*i) % m == 1) {
            if(i > x) {
                x = i;
            }
        }

        i++;
    }

    cout << x;
    return 0;
}