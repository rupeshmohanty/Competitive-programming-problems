// Question Link: https://practice.geeksforgeeks.org/problems/geeksforgeeks/0/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        queue<int> q;

        for(int i = 1;i <= n;i++) {
            q.push(i);
        }

        while(q.size() != 1) {
            q.push(q.front());
            q.pop();
            q.pop();
        }

        cout << q.front() << endl;
    }
    return 0;
}