#include <bits/stdc++.h>
using namespace std;

void update(int l,int r,int x,int A[4]){
    for(int i = l;i <= r;i++) {
        A[i] += x;
    }
}

void printArray(int A[4]) {
    for(int i = 0;i< 4;i++) {
        cout << A[i] << " ";
    }
    cout << endl;
}

int main() {
    int A[4] = {10,5,20,40};

    update(0,1,10,A);
    printArray(A);
    update(1,3,20,A);
    update(2,2,30,A);
    printArray(A);

    return 0;
}