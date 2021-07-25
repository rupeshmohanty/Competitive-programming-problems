// Question Link: https://practice.geeksforgeeks.org/problems/k-consecutive-odd-elements/0/
#include <bits/stdc++.h>
using namespace std;

bool countOdd(int a[],int len,int num) {
    int count = 0;
    int max = 0;
    sort(a,a+len);

    for(int i = 0;i < len;i++) {
        if(a[i] % 2 != 0) {
            count++;
            if(count > max) {
                max = count;
            }
        } else {
            count = 0;
        }
    }

    if(max >= num) {
        return true;
    } else {
        return false;
    }
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n,k;
        cin >> n >> k;
        int arr[n];
        bool res = false;

        for(int i = 0;i < n;i++) {
            cin >> arr[i];
        }

        res = countOdd(arr,n,k);
        if(res) {
            cout << "yes";
        } else {
            cout << "no";
        }
        cout << endl;
    }
    return 0;
}