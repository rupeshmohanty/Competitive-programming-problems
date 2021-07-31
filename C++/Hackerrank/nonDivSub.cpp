#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,k;
    int s[n];

    cin >> n >> k;

    for(int i = 0;i < n;i++) {
        cin >> s[i];
    }

    set<int> temp;

    for(int i = 0;i < n;i++) {
        for(int j = 0;j < n;j++) {
            if(i != j) {
                if(s[i] + s[j] % k != 0) {
                    temp.emplace(s[i]);
                    temp.emplace(s[j]);            
                }
            }
        }
    }

    cout << temp.size();
    return 0;
}