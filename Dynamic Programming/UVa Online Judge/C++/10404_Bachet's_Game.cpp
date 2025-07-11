#include <iostream>
using namespace std;

const int MAXN = 1000001;
bool dp[MAXN];
int M[100];
int k;

void solve(int n) {
    for (int i = 0; i <= n; ++i) {
        dp[i] = false;
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < k; ++j) {
            int m = M[j];
            if (m > i) {
                continue;
            }
            if (!dp[i - m]) {
                dp[i] = true;
                break;
            }
        }
    }
    if (dp[n]) {
        cout<<"Stan wins"<<endl;
    } else {
        cout<<"Ollie wins"<<endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    while (cin >> n) {
        if (!(cin >> k)) {
            break;
        }
        for (int i = 0; i < k; ++i) {
            cin >> M[i];
        }
        solve(n);
    }
    return 0;
}
