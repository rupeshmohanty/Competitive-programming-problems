#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    int arr[n];
    vector<int> vec;

    cin >> n;
    for(int i = 0;i < n;i++) {
        cin >> arr[i];
    }

    for(int i = 0;i < n;i++) {
        if(arr[i] % 10 != 0) {
            vec.emplace_back(arr[i]);
        }
    }

    for(int i = 0;i < n;i++) {
        if(arr[i] % 10 == 0) {
            vec.emplace_back(arr[i]);
        }
    }

    for(auto it:vec) {
        cout << it << " ";
    }
    return 0;
}