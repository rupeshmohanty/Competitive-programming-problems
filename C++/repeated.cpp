#include <bits/stdc++.h>
using namespace std;

bool checkNum(int num) {
    set<int> s;
    int temp = 0;
    string st = to_string(num);

    while(num > 0) {
        temp = num % 10;
        s.emplace(temp);
        num = num / 10;
    }

    if(s.size() == st.length()) {
        return true;
    } else {
        return false;
    }
    
}

int main() {
    int n1,n2;
    cin >> n1;
    cin >> n2;
    bool res = false;
    int count = 0;

    for(int i = n1;i <= n2;i++) {
        res = checkNum(i);
        if(res) {
            count++;
        }
    }

    cout << count;
    return 0;
}