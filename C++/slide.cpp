#include<bits/stdc++.h>
using namespace std;

int main() {
    int n,k;
    int arr[n];
    string s = "";

    cin >> n;
    
    for(int i = 0;i < n;i++) {
        cin >> arr[i];
    }

    cin >> k;

    for(int i = k;i < n;i++) {
        s = s + to_string(arr[i]) + " ";
    }

    for(int i = 0;i < k;i++) {
        s = s + to_string(arr[i]) + " ";
    }

    cout << s;

    return 0;
}