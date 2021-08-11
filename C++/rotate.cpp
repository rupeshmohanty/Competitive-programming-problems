#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,k;
    int arr[n];

    cin >> n;

    for(int i = 0;i < n;i++) {
        cin >> arr[i];
    }

    cin >> k;
    vector<int> vec;

    for(int i = n-k;i < n;i++) {
        vec.emplace_back(arr[i]);
    }

    for(int j = 0;j < n-k;j++) {
        vec.emplace_back(arr[j]);
    }

    for(auto it: vec) {
        cout << it << " ";
    }

    return 0;
}