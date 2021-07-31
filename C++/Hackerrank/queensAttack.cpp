#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,k,r,c;

    cin >> n >> k;
    cin >> r >> c;

    int arr[n][n];
    int count = 0;
    // Counting the total number of moves that the queen can play without the obstacles!
    for(int i = 1;i <= n;i++) {
        for(int j = 1;j <= n;j++) {
            if(i == r) {
                count++;
            } else if(j == c) {
                count++;
            } else if (i+j == r+c) {
                count++;
            } else if (i - j == r - c) {
                count++;
            } else {
                continue;
            }
        }
    }

    int obs = 0;
    while(k > 0) {
        int a,b;
        cin >> a >> b;
        
        for(int i = 1;i <= n;i++) {
            for(int j = 1;j <= n;i++) {
                if(r == a) {
                    if(j <= b) {
                        obs++;
                    }
                } else if(c == b) {
                    if(i <= a) {
                        obs++;
                    }
                }
            }
        }

        k--;
    }

    cout << (count - obs);

    return 0;
}