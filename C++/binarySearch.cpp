// Question Link: geeksforgeeks.org/binary-search/
#include <bits/stdc++.h>
using namespace std;

int binarySearch(int a[],int l,int r,int num) {
    int mid;
    if(r >= l) {
        mid = l + (r-1) / 2;

        if(a[mid] == num) {
            return mid;
        } 

        if(a[mid] > num) {
            return binarySearch(a,l,mid - 1,num);
        }

        return binarySearch(a,mid+1,r,num);
    }

    return -1;
}

int main() {
    int arr[10] = {10,20,30,40,50,60,70,110,120,130};
    int x = 110;
    int len = sizeof(arr)/sizeof(arr[0]);
    int res = 0;

    res = binarySearch(arr,0,len-1,x);
    if(res >= 0) {
        cout << "Element found at: " << res;
    } else {
        cout << "Unable to find the element";
    }

    return 0;
}