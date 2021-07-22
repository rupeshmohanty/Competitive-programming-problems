#include <bits/stdc++.h>
using namespace std;

int main() {
    int s,v1,v2,t1,t2;
    cin >> s >> v1 >> v2 >> t1 >> t2;
    int score1 = 0, score2 = 0;

    score1 = s*v1 + 2*t1;
    score2 = s*v2 + 2*t2;

    if(score1 < score2) {
        cout << "First";
    } else if (score1 > score2) {
        cout << "Second";
    } else {
        cout << "Friendship";
    }
    return 0;
}