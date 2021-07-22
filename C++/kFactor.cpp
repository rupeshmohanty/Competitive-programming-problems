// Question Link: https://practice.geeksforgeeks.org/problems/kth-smallest-factor2345/1
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,k;
    cin >> n >> k;
    vector<int> arr;

    for(int i = 1;i <= n;i++) {
        if(n % i == 0) {
            arr.push_back(i);
        }
    }

    if(arr.size() < k) {
        cout << -1;
    } else {
        cout << arr[k-1];
    }
    return 0;
}