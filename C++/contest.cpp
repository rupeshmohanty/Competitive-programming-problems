// Question link : https://codeforces.com/problemset/problem/999/A
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,k;
    cin >> n >> k;
    vector<int> arr;
    int count = 0;

    // entering an array!
    for(int i = 0;i < n;i++) {
        int x;
        cin >> x;
        arr.emplace_back(x);
    }

    int j = 0;
    while(j < n) {
        if(j % 2 == 0) {
            if(arr.at(arr.size()-1) <= k) {
                arr.pop_back();
            }
        } else {
            if(arr.at(0) <= k) {
                arr.erase(arr.begin());
            } 
        }
        j++;
    }
    cout << (n-arr.size());
    return 0;
}