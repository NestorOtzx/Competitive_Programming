//Currently timelimit, should change the memorization technique or migrate to tabulation, but the logic is ok.
#include <iostream>
#include <vector>
#include <limits>
#include <cstring>
#include <unordered_map>
#include <string>
using namespace std;

const int INF = 1e9;
vector<pair<int, int>> G[100];
vector<int> A;
int suma;
int f;
unordered_map<string, int> memo;

bool dfs(int v, int p) {
    if (v == f) return true;

    for (auto& [u, c] : G[v]) {
        if (u != p && dfs(u, v)) {
            A.push_back(c);
            suma += c;
            return true;
        }
    }
    return false;
}

int phi(int n, int c) {
    string key = to_string(n) + "," + to_string(c);
    if (memo.count(key)) return memo[key];

    int ans;
    if (n == 1 && c == 0) ans = 0;
    else if (n == 1 && c != 0) ans = INF;
    else if (n != 1 && c == 0) ans = 0;
    else {
        if (A[n - 1] <= c) {
            ans = min(phi(n, c - A[n - 1]) + 1, phi(n - 1, c));
        } else {
            ans = phi(n - 1, c);
        }
    }

    memo[key] = ans;
    return ans;
}

void solve(int u, int v, int c) {
    A.clear();
    suma = 0;
    f = v;
    dfs(u, -1);

    int ans = INF;
    if (c - suma >= 0 && !A.empty() && (c - suma) % 2 == 0) {
        ans = phi(A.size(), (c - suma) / 2) * 2 + A.size();
    }

    if (ans < INF) {
        cout << "Yes " << ans << '\n';
    } else {
        cout << "No\n";
    }
}

string read_non_empty_line() {
    string line;
    while (getline(cin, line)) {
        if (!line.empty()) return line;
    }
    return "";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    T = stoi(read_non_empty_line());

    for (int t = 0; t < T; ++t) {
        int n, M;
        {
            string line = read_non_empty_line();
            sscanf(line.c_str(), "%d %d", &n, &M);
        }

        for (int i = 0; i < n; ++i) G[i].clear();

        for (int i = 0; i < M; ++i) {
            int u, v, c;
            cin >> u >> v >> c;
            G[u - 1].emplace_back(v - 1, c);
            G[v - 1].emplace_back(u - 1, c);
        }

        int K;
        cin >> K;
        for (int i = 0; i < K; ++i) {
            int u, v, c;
            cin >> u >> v >> c;
            memo.clear();
            solve(u - 1, v - 1, c);
        }

        if (t < T - 1) cout << '\n';
        string dummy;
        getline(cin, dummy); 
    }

    return 0;
}
