// Question Link: https://codeforces.com/problemset/problem/1284/A
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,m;
    cin >> n >> m;
    string s1,s2;

    cin >> s1;
    cin >> s2;

    int q;
    cin >> q;
    while(q--) {
        int y;
        cin >> y;

        cout << s1[y%n] + s2[y%m]; 
    }
    return 0;
}