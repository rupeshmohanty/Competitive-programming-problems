// Question Link: https://practice.geeksforgeeks.org/problems/k-larger-values-1611827113/0/#
#include <bits/stdc++.h>
using namespace std;

void largestElements(set<int> a,int num) {
    auto len = a.size();
    if(len < num) {
        cout << -1;
    } else {
        int count = 0;
        for(auto i = a.rbegin();i != a.rend();i++,count++) {
            if(count == num)
                break;
            
            cout << *i << " ";
        }
    }
}

int main() {
    int t;
    cin >> t;
    while(t--){
        int n,k;
        cin >> n >> k;
        set<int> arr;

        for(int i = 0;i < n;i++) {
            int x;
            cin >> x;
            arr.insert(x);
        }

        largestElements(arr,k);
        cout << endl;
    }
    return 0;
}