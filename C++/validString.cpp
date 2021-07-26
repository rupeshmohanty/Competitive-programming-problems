// Question Link: https://practice.geeksforgeeks.org/problems/valid-string/0/#
#include <bits/stdc++.h>
using namespace std;

bool checkString(string str,int num) {
    int count0 = 0,count1 = 0;
    int check = 0;
    for(int i = 0;i < num;i++) {
        if(str[i] == '0') {
            count0++;
        } else {
            count1++;
        }

        if(count0 < count1) {
            check = 1;
            break; 
        }
    }

    if(check > 0) {
        return false;
    } else {
        if(count0 == count1) {
            return true;
        } else {
            return false;
        }
    }
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        bool res = false;

        res = checkString(s,n);
        if(res) {
            cout << "yes";
        } else {
            cout << "no";
        }
        cout << endl;
    }
    return 0;
}