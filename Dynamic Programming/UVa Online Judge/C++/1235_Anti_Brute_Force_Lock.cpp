#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <limits>
#include <cmath>
using namespace std;

const int MAX = 505;
const int INF = 1e9;

vector<pair<int, int>> G[MAX];
int c[MAX];
bool vis[MAX];

int dist(const string& a, const string& b) {
    int ans = 0;
    for (int i = 0; i < 4; ++i) {
        int x = a[i] - '0';
        int y = b[i] - '0';
        int diff = abs(x - y);
        ans += min(diff, 10 - diff);
    }
    return ans;
}

int dist0(const string& a) {
    int ans = 0;
    for (int i = 0; i < 4; ++i) {
        int d = a[i] - '0';
        ans += min(d, 10 - d);
    }
    return ans;
}

int prim(int nodo, int tamG) {
    for (int i = 1; i <= tamG; ++i) {
        c[i] = INF;
        vis[i] = false;
    }

    c[nodo] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, nodo));
    int ans = 0;
    int cont = 0;

    while (!pq.empty() && cont < tamG) {
        int du = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (!vis[u]) {
            vis[u] = true;
            ans += du;
            cont++;
            for (size_t i = 0; i < G[u].size(); ++i) {
                int v = G[u][i].first;
                int cost = G[u][i].second;
                if (!vis[v] && cost < c[v]) {
                    c[v] = cost;
                    pq.push(make_pair(c[v], v));
                }
            }
        }
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    string line;
    getline(cin, line);
    T = stoi(line);

    for (int t = 0; t < T; ++t) {
        getline(cin, line);
        istringstream iss(line);
        vector<string> codes;
        string s;
        while (iss >> s) {
            codes.push_back(s);
        }

        int n = stoi(codes[0]); 
        codes.erase(codes.begin()); 

        int salirDe0 = INF;
        for (int i = 0; i < n; ++i) {
            int d = dist0(codes[i]);
            if (d < salirDe0) {
                salirDe0 = d;
            }
        }

        for (int i = 1; i <= n; ++i) {
            G[i].clear();
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j) {
                    int d = dist(codes[i], codes[j]);
                    G[i + 1].push_back(make_pair(j + 1, d));
                }
            }
        }

        int mst = prim(1, n);
        cout << mst + salirDe0 << '\n';
    }

    return 0;
}
