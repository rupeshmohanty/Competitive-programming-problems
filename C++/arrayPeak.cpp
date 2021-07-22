#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n,k,count = 0;
        cin >> n >> k;
        vector<int> arr;
        
        if(n == 1) {
            arr.push_back(1);
        } else {
            if(k < n/2) {
                for(int i = 1;i <= arr.size();i++) {
                    arr.push_back(i);
                    arr.push_back(i+1);
                    count++;

                    if(count == k) {
                        break;
                    }
                }
            }
        }

        if(arr.size() == n) {
            // printing the resultant array!
            for(auto it:arr) {
                cout << it << " ";
            }
            cout << endl;
        } else {
            cout << -1 << endl;
        }
        
    }
    return 0;
}