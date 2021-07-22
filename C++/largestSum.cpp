// Question Link: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    vector<int> arr = {-2,-3,4,-1,-2,1,5,-3};
    int max_sum = INT_MIN;
    int change_sum = 0;

    for(int i = 0;i < arr.size();i++) {
        change_sum += arr.at(i);
        if(change_sum > max_sum) {
            max_sum = change_sum;
        } 

        if(change_sum < 0) {
            change_sum = 0;
        }
    }

    cout << max_sum;
    return 0;
}