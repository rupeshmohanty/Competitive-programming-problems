#include <bits/stdc++.h>
using namespace std;

int factor(int num) {
    for(int i = 2; i<num;i++) {
        if(num%i == 0) {
            return i;
        }
    }
}

int main() {
    int a,b;
    cin >> a >> b;
    int s = a;
    bool flag = false;
    int res = 0;

    int i = 1;
    while(i <= a){
        res = factor(s);
        s += res;

        if(s == b){
            flag = true;
            break;
        }
        i += 1;
    }

    if(flag) {
        cout << "Yes";
    } else {
        cout << "No";
    }

    return 0;
}