#include <bits/stdc++.h>
using namespace std;

int main() {
    int vec[5] = {1,2,3,5,6};
    int x = 5;

    int ind = lower_bound(vec,vec+5,x) - vec;

    if(ind != 5 && vec[ind] == x){
        cout << "Element found at " << ind << endl;
    } else {
        cout << "Unable to find element!";
    }
    return 0;
}
