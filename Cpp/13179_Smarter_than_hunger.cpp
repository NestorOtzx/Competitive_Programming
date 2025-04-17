#include <iostream>
#include <string>

using namespace std;

pair<int, int> B[102];
int F;

int dist(int inda, int indb) {
    return abs(B[inda].first - B[indb].first) + abs(B[inda].second - B[indb].second);
}

int dp[103][103][151];

int phitab(int RT)
{
    for (int m1 = F; m1>= 0; m1--)
    {
        for (int m2 = F; m2>= 0; m2--)
        {
            for (int rt = RT; rt >= 0; rt--)
            {
                if (m1 == F && m2 == F) {
                    dp[m1][m2][rt] = 1;
                } else {
                    if (m1 == F) {
                        int cost = max(dist(m2, F) - rt, 0);
                        dp[m1][m2][rt] = cost + dp[m1][F][0];
                    } else if (m2 == F) {
                        int cost = max(dist(m1, F) - rt, 0);
                        dp[m1][m2][rt] = cost + dp[F][m2][0];
                    } else {
                        int n = max(m1, m2);
                        int rt1 = 0, rt2 = 0;
                        if (m1<m2)
                        {   
                            rt1 = rt;
                        }else{
                            rt2 = rt;
                        }
                        int dm1 = max(dist(m1, n + 1) - rt1, 0);
                        int dm2 = max(dist(m2, n + 1) - rt2, 0);
                        dp[m1][m2][rt] = min(dm1 + dp[n+1][m2][dm1+rt2], dm2 + dp[m1][n+1][dm2+rt1]);
                    }
                }
            }
        }
    }
    return dp[0][0][0];
}

int main() {
    string line;
    int R, C, N;
    while (getline(cin, line) && !line.empty()) {
        sscanf(line.c_str(), "%d %d", &R, &C);
        cin >> N;
        B[0] = {1, 1};

        for (int n = 1; n <= N; ++n) {
            int a, b;
            cin >> a >> b;
            B[n] = {a, b};
        }

        F = N + 1;
        B[F] = {R, C};

        cout << phitab(min(R*C, 150)) << endl;

        cin.ignore();
    }

    return 0;
}
