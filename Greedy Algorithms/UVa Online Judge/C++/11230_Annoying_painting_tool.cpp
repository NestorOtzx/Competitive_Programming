#include <iostream>
#include <string>
using namespace std;

int N, M, R, C;
int MAT[101][101];

bool isok() {
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            if (MAT[i][j] != 0)
                return false;
    return true;
}

void paint(int x, int y) {
    if (x + C <= M && y + R <= N) {
        for (int i = y; i < y + R; ++i)
            for (int j = x; j < x + C; ++j)
                MAT[i][j] ^= 1;
    }
}

int phi(int x, int y) {
    if (x == 0 && y == N) return 0;
    if (x == M && y != N) return phi(0, y + 1);
    if (x != M && MAT[y][x] == 1) {
        paint(x, y);
        return phi(x + 1, y) + 1;
    }
    if (x != M && MAT[y][x] == 0) return phi(x + 1, y);
    return 0;
}

void solve() {
    int res = phi(0, 0);
    if (!isok()) res = -1;
    cout << res << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (cin >> N >> M >> R >> C, N + M > 0) {
        string line;
        for (int i = 0; i < N; ++i) {
            cin >> line;
            for (int j = 0; j < M; ++j)
                MAT[i][j] = line[j] - '0';
        }
        solve();
    }

    return 0;
}
