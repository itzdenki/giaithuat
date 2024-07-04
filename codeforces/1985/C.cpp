#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),vrend()
#define pb push_back 
#define INF 1000000000
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
const int MAX = 200'007;
const int MOD = 1'000'000'007;
#define rep(i,s,e) for(int i=s;i<e;i++)
void read_vi(vi &a,int n){rep(i,0,n)cin >> a[i];}
void read_vll(vll &a,int n){rep(i,0,n)cin >> a[i];}

void solve()
{
    int n;
    cin >> n;
    vll a(n);
    read_vll(a, n);
    
    ll sum = 0;
    ll mx = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i];
        mx = max(mx, a[i]);
        if (sum - mx == mx) ans++;
    }

    cout << ans << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++)
    {
        solve();
    }
}