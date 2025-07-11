#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

const int MAX = 10000;
int r, c, q;
vector<set<int>> G(MAX);
vector<vector<int>> Gpuentes(MAX);
int visited[MAX], low[MAX], p[MAX], blqsNodos[MAX];
int t, bloques;

void bridgesAux(int v) {
    visited[v] = low[v] = ++t;

    for (int w : G[v]) {
        if (visited[w] == -1) {
            p[w] = v;
            bridgesAux(w);
            low[v] = min(low[v], low[w]);

            if (low[w] > visited[v]) {
                Gpuentes[v].push_back(w);
                Gpuentes[w].push_back(v);
            }
        } else if (w != p[v]) {
            low[v] = min(low[v], visited[w]);
        }
    }
}

void bridgesTarjan() {
    for (int v = 0; v < r; ++v) {
        visited[v] = -1;
        low[v] = -1;
        p[v] = -1;
    }

    t = 0;
    for (int i = 0; i < r; ++i) {
        if (visited[i] == -1) {
            bridgesAux(i);
        }
    }
}

void dfsAux(int v) {
    visited[v] = 0;
    blqsNodos[v] = bloques;

    for (int u : Gpuentes[v]) {
        if (visited[u] == -1) {
            dfsAux(u);
        }
    }
}

void dfs() {
    bloques = 0;
    for (int v = 0; v < r; ++v) {
        visited[v] = -1;
        blqsNodos[v] = 0;
    }

    for (int v = 0; v < r; ++v) {
        if (visited[v] == -1) {
            ++bloques;
            dfsAux(v);
        }
    }
}

void solve(int ini, int fin) {
    if (blqsNodos[ini] == blqsNodos[fin]) {
        cout << "Y\n";
    } else {
        cout << "N\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (cin >> r >> c >> q, r + c + q > 0) {
        for (int v = 0; v < r; ++v) {
            G[v].clear();
            Gpuentes[v].clear();
        }

        for (int i = 0; i < c; ++i) {
            int u, v;
            cin >> v >> u;
            --v; --u;
            G[v].insert(u);
            G[u].insert(v);
        }

        bridgesTarjan();
        dfs();

        for (int i = 0; i < q; ++i) {
            int ini, fin;
            cin >> ini >> fin;
            solve(ini - 1, fin - 1);
        }

        cout << "-\n";
    }

    return 0;
}
