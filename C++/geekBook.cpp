// Question Link: https://practice.geeksforgeeks.org/problems/geek-and-books/0/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        stack<int> st;
        
        while(n--) {
            string s;
            cin >> s;
            vector<int> vec;

            if(s == "remove") {
                if(!st.empty()) {
                    vec.emplace_back(st.top());
                    st.pop();
                } else {
                    vec.emplace_back(-1);
                }
            } else {
                for(int i = 0;i < s.length()-1;i++) {
                    if(s[i] >= 'a' and s[i] <= 'z') {
                        continue;
                    } else {
                        st.push(s[i]);
                    }
                }
            }

            for(auto it = vec.begin();it != vec.end();it++) {
                cout << *it << " ";
            }
        }

        cout << endl;
    }
    return 0;
}