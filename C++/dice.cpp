#include <bits/stdc++.h>
#include <cmath>
using namespace std;

int main() {
    int a,b,count1 = 0, count2 = 0, count3 = 0;  
    cin >> a >> b;
    
    for(int i = 1;i<=6;i++) {
        if(abs(i-a) < abs(i-b)) {
            count1 += 1;
        } else if (abs(i-a) > abs(i-b)) {
            count2 += 1;
        } else {
            count3 += 1;
        }
    }

    cout << count1 << " " << count3 << " " << count2;
    return 0;
}