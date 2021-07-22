#include <bits/stdc++.h>
using namespace std;

void update(int a[],int n,int res[],int k) {
    // changing the elements!
    for(int i = 0;i < k;i++) {
        for(int j = a[i]-1;j < n;j++) {
            res[j] += 1;
        }
    }
}

int main() {
    int n,k;
    cin >> n >> k;
    int A[k];
    int res[n] = {0};

    // add elements to the array!
    for(int i = 0;i < k;i++) {
        cin >> A[i];
    }

    update(A,n,res,k);

    for(int i = 0;i < n;i++) {
        cout << res[i] << " ";
    }

    return 0;
}