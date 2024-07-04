#include <bits/stdc++.h>
using namespace std;
typedef int64_t ll;
ll mx = INT64_MAX;
ll mn = INT64_MIN;
#define REP(i,j,k) for(ll (i)=(j);(i)<(k);++(i))

void solved() {
    int n, m;
    cin >> n >> m;
    string s;
    int cont = 0;
    int x = 0, y = 0;
    REP(i, 0, n) {
        bool empieza = true;
        int aux = 0, primero = 0, ultimo = 0;
        cin >> s;
        REP(j, 0, s.length()) {
            if (s[j] == '#') {
                aux++;
                if (empieza) {
                    primero = j;
                    empieza = false;
                }
                ultimo = j;
            }
        }
        if (aux > cont) {
            cont = aux;
            x = i + 1;
            y = primero + 1 + ((ultimo - primero) / 2);
        }
    }
    cout << x << " " << y << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cout << fixed;
    int t;
    cin >> t;
    while (t--) {
        solved();
    }
}