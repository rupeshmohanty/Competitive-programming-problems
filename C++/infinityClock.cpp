// Question Link: https://codeforces.com/problemset/problem/1392/B
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    while(t--) {
        int n,k;
        cin >> n >> k;
        vector<int> arr;
        
        // enter the elements into the arr!
        for(int i = 0;i < n;i++) {
            int x;
            cin >> x;
            arr.emplace_back(x);
        }

        while(k--) {
            // maximum element!
            int d = INT_MIN;
            for(int i = 0;i < n;i++) {
                d = max(d,arr[i]);
            }

            // modifying the elements!
            for(int j = 0;j < n;j++) {
                arr[j] = d - arr[j];
            }
        }
        // display the final array!
        for(int p = 0;p < n;p++) {
            cout << arr[p] << " ";
        }
    }
    return 0;
}