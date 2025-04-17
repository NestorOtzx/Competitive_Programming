#include <iostream>
#include <vector>
#include <unordered_map>
#include <tuple>
#include <cmath>
#include <string>

using namespace std;

pair<int, int> B[102];
int N, R, C, F;

struct KeyHasher {
    size_t operator()(const tuple<int, int, int, int>& key) const {
        auto [a, b, c, d] = key;
        size_t h1 = hash<int>{}(a);
        size_t h2 = hash<int>{}(b);
        size_t h3 = hash<int>{}(c);
        size_t h4 = hash<int>{}(d);
        return ((h1 ^ (h2 << 1)) >> 1) ^ (h3 << 1) ^ (h4 << 2);
    }
};

unordered_map<tuple<int, int, int, int>, int, KeyHasher> memo;

int dist(int inda, int indb) {
    return abs(B[inda].first - B[indb].first) + abs(B[inda].second - B[indb].second);
}

int phi(int m1, int m2, int rt1, int rt2) {
    tuple<int, int, int, int> key = make_tuple(m1, m2, rt1, rt2);

    if (memo.count(key)) return memo[key];

    int ans;
    if (m1 == F && m2 == F) {
        ans = 1;
    } else {
        if (m1 == F) {
            int cost = max(dist(m2, F) - rt2, 0);
            ans = cost + phi(m1, F, 0, 0);
        } else if (m2 == F) {
            int cost = max(dist(m1, F) - rt1, 0);
            ans = cost + phi(F, m2, 0, 0);
        } else {
            int n = max(m1, m2);
            int dm1 = max(dist(m1, n + 1) - rt1, 0);
            int dm2 = max(dist(m2, n + 1) - rt2, 0);
            ans = min(dm1 + phi(n + 1, m2, 0, dm1 + rt2), dm2 + phi(m1, n + 1, dm2 + rt1, 0));
        }
    }

    memo[key] = ans;
    return ans;
}

int main() {
    string line;
    while (getline(cin, line) && !line.empty()) {
        sscanf(line.c_str(), "%d %d", &R, &C);
        cin >> N;
        B[0] = {1, 1};
        memo.clear();

        for (int n = 1; n <= N; ++n) {
            int a, b;
            cin >> a >> b;
            B[n] = {a, b};
        }

        F = N + 1;
        B[F] = {R, C};

        cout << phi(0, 0, 0, 0) << endl;

        cin.ignore(); // consumir newline sobrante
    }

    return 0;
}
