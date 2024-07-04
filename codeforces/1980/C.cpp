#include <bits/stdc++.h>
#define endl '\n'
#define int long long
using namespace std;

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> ori(n);
        vector<int> kw(n);
        vector<int> change;
        for (auto& i : ori) cin >> i;
        for (auto& i : kw) cin >> i;
        for (int i = 0; i < n; i++) {
            if (ori[i] != kw[i]) {
                change.push_back(kw[i]);
            }
        }
        int m, x = 0;
        cin >> m;
        vector<int> modify(m);
        sort(change.begin(), change.end());
        for (int i = 0; i < m; i++) {
            cin >> modify[i];
        }
        int last = modify[m - 1];
        bool gate = false;
        if (find(kw.begin(), kw.end(), last) != kw.end()) gate = true;
        sort(modify.begin(), modify.end());
        for (int i = 0; i < m && x < change.size(); ) {
            if (change[x] == modify[i]) {
                x++;
                i++;
            } else {
                i++;
            }
        }
        x = change.size() - x;
        if (x == 0) {
            if (gate) cout << "YES" << endl;
            else cout << "NO" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}