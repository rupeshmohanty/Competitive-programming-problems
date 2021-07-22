#include <bits/stdc++.h>
using namespace std;

int main() {
    int arr[10] = {1,2,3,4,5,10,10,10,11,12};
    int x = 10;

    int ind = upper_bound(arr,arr+10,x) - arr - 1;
    if(ind >= 0 && arr[ind] == x){
        cout << ind;
    } else {
        cout << "No such element present";
    }
    return 0;
}