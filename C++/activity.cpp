// Question Link: https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
#include <bits/stdc++.h>
using namespace std;

void task(int s[],int f[]) {
    int count = 0;
    vector<int> arr = {0};

    for(int i = 1;i < 3;i++) {
        if(abs(s[i] - f[i]) < abs(s[i-1] - f[i-1])) {
            arr.emplace_back(i);
            count++;
        }
    } 

    // print the array!
    for(auto j:arr) {
        cout << j << " ";
    }
}

int main() {
    int start[3] = {10,12,20},finish[3] = {20,25,30};
    task(start,finish);
    return 0;
}