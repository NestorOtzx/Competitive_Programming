#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

const int MAXN = 100001;
const int INF = 1e9 + 7;
const int MAXINPUT = 31;

int tree[MAXN * 2];
int n;

void build(const vector<int>& a, int v, int l, int r) {
    if (l == r) {
        tree[v] = a[l];
    } else {
        int m = l + ((r - l) >> 1);
        build(a, v + 1, l, m);
        build(a, v + 2 * (m - l + 1), m + 1, r);
        tree[v] = min(tree[v + 1], tree[v + 2 * (m - l + 1)]);
    }
}

int query(int v, int L, int R, int l, int r) {
    if (l > r) return INF;
    if (l == L && r == R) return tree[v];
    int m = L + ((R - L) >> 1);
    return min(
        query(v + 1, L, m, l, min(r, m)),
        query(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r)
    );
}

void update(int v, int L, int R, int pos, int h) {
    if (L == R) {
        tree[v] = h;
    } else {
        int m = L + ((R - L) >> 1);
        if (pos <= m) {
            update(v + 1, L, m, pos, h);
        } else {
            update(v + 2 * (m - L + 1), m + 1, R, pos, h);
        }
        tree[v] = min(tree[v + 1], tree[v + 2 * (m - L + 1)]);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> n >> q;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) cin >> arr[i];

    build(arr, 0, 0, n - 1);

    cin.ignore();
    string line;
    while (q--) {
        getline(cin, line);

        if (line.substr(0, 5) == "query") {
            line = line.substr(6, line.length() - 7);
            replace(line.begin(), line.end(), ',', ' ');
            int a, b;
            stringstream ss(line);
            ss >> a >> b;
            cout << query(0, 0, n - 1, a - 1, b - 1) << '\n';
        } else { 
            line = line.substr(6, line.length() - 7); 
            replace(line.begin(), line.end(), ',', ' ');
            stringstream ss(line);
            vector<int> indices;
            int idx;
            while (ss >> idx) {
                indices.push_back(idx - 1);
            }

            vector<int> values(indices.size() + 1);
            for (size_t i = 0; i < indices.size(); ++i) {
                values[i] = arr[indices[i]];
            }
            values[indices.size()] = values[0];

            for (size_t i = 0; i < indices.size(); ++i) {
                arr[indices[i]] = values[i + 1];
                update(0, 0, n - 1, indices[i], values[i + 1]);
            }
        }
    }

    return 0;
}
