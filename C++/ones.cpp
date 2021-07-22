#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n,m;
        cin >> n >> m;
        int a[n][m];

        for(int i = 1;i <= n;i++) {
            for(int j = 1;j <= n;j++) {
                cin >> a[i][j];
            }
        }

        int q;
        cin >> q;

        while(q--) {
            int r1,c1,r2,c2;
            cin >> r1 >> c1 >> r2 >> c2;
            int count = 0;
            int i = 1,j = 1;

            for(i = min(r1,r2);i <= max(r1,r2);i++) {
                for(j = min(c1,c2);j <= max(c1,c2);j++) {
                    if(a[i][j] == 1) {
                        count++;
                    }
                }
            }
            cout << count << endl;
        }
    }
    return 0;
}