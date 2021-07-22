#include <bits/stdc++.h>
using namespace std;

int main() {
    int arr[5] = {1,2,2,3,4};
    int x = 2;

    int cnt = count(arr,arr+5,x);
    cout << cnt;
    return 0;
}