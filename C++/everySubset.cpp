// Question Link: https://codeforces.com/problemset/problem/1323/A
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        int arr[n];
        bool flag = false;
        int oc = 0;
        vector<int> pos;

        for(int i = 0;i < n;i++) {
            cin >> arr[i];
        }

        for(int i = 0;i < n;i++) {
            if(arr[i] % 2 == 0) {
                flag = true;
                cout << 1 << endl;
                cout << (i+1);
                break;
            } else {
                oc += 1;
                pos.push_back(i+1);
                if(oc == 2) {
                    cout << oc << endl;
                    for(int i = 0;i < pos.size();i++) {
                        cout << pos[i] << " ";
                    }
                    flag = true;
                    break;
                }
            }
        }
        if(flag == false) {
            cout << -1;
        }
        cout << endl;
    }
    return 0;
}