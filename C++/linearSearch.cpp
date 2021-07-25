// Question Link: https://www.geeksforgeeks.org/linear-search/
#include <bits/stdc++.h>
using namespace std;

int lsearch(int a[],int len,int ele) {
    for(int i = 0;i < len;i++) {
        if(a[i] == ele) {
            return i;
        }
    }

    return -1;
}

int main() {
    int n,x;
    int res = 0;
    cin >> n;
    
    int arr[n];
    for(int i = 0;i < n;i++) {
        cin >> arr[i];
    }
    
    cin >> x;

    res = lsearch(arr,n,x);
    cout << res;
    return 0;
}