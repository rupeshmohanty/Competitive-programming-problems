#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n,k;
        cin >> n >> k;
        string s = "";
        string temp = "abc";

        for(int i = 0;i < k;i++) {
            s += "a";
        }

        for(int i = k;i < n;i++) {
            if(i % 2 == 0) {
                s += "b";
            } else {
                s += "ca";
            }
        }

        cout << s << endl;
    }
    return 0;
}