// Question Link: https://practice.geeksforgeeks.org/problems/contest-score/0/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        int arr[n];

        // input array!
        for(int i = 0;i < n;i++) {
            cin >> arr[i];
        }

        for(int i = 0;i < n;i++) {
            bool flag = false;
            for(int j = i;j < n;j++) {
                if(arr[j] < arr[i]) {
                    arr[i] = j+1;
                    flag = true;
                    break;
                } 
            }
            if(flag == false) {
                arr[i] = -1;
            }
        }

        // resultant array!
        for(int i = 0;i < n;i++) {
            cout << arr[i] << " ";
        }

        cout << endl;
    }
    return 0;
}