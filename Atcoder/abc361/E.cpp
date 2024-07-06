#include <bits/stdc++.h>
using namespace std;
#define int long long

const int maxn = 2e5 + 5;
int n;
int x, y, z;
vector<pair<int, int>> g[maxn];
int dp[maxn];
int ans;
int jl;

void dfs(int x, int fa) {
    if (ans < dp[x]) {
        ans = dp[x];
        jl = x;
    }
    for (int i = 0; i < g[x].size(); i++) {
        int v = g[x][i].first;
        if (v == fa) {
            continue;
        }
        dp[v] = dp[x] + g[x][i].second;
        dfs(v, x);
    }
}

signed main() {
    scanf("%lld", &n);
    int tot = 0;
    for (int i = 1; i < n; i++) {
        scanf("%lld %lld %lld", &x, &y, &z);
        tot += z;
        g[x].push_back(make_pair(y, z));
        g[y].push_back(make_pair(x, z));
    }
    ans = 0;
    dp[1] = 0;
    dfs(1, 0);
    ans = 0;
    dp[jl] = 0;
    dfs(jl, 0);
    printf("%lld", tot * 2 - ans);
}
