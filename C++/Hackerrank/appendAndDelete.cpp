// Question Link: https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen
#include <bits/stdc++.h>
using namespace std;

string appendAndDelete(string s, string t, int k) {
    int count = 0;

    for(int i = 0;i < s.length();i++) {
        if(t.find(s[i])) {
            continue;
        } else {
            s.erase(i);
            count++;
        }
    }

    for(int i = 0;i < t.length();i++) {
        if(s.find(t[i])) {
            continue;
        } else {
            s.push_back(t[i]);
            count++;
        }
    }   

    if(count <= k) {
        return "Yes";
    } else {
        return "No";
    }
}

int main() {
    string s,t;
    int k;

    cin >> s;
    cin >> t;
    cin >> k;

    string res = "";

    res = appendAndDelete(s,t,k);
    cout << res;
}