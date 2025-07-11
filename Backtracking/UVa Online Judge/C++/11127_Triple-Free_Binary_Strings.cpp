#include <iostream>
#include <string>
using namespace std;

string P;
int ans;

bool check(const string& word) {
    int fin = word.size();
    if (fin < 3) return true;

    int slen = fin / 3;
    for (int i = 1; i <= slen; ++i) {
        int a = fin - i;
        int b = a - i;
        int c = b - i;
        if (c < 0) break;
        if (word.substr(c, i) == word.substr(b, i) &&
            word.substr(b, i) == word.substr(a, i)) {
            return false;
        }
    }
    return true;
}

void backtrack(int n, string word) {
    if (n == P.length()) {
        ans++;
    } else {
        if (P[n] == '*') {
            word.push_back('0');
            if (check(word)) backtrack(n + 1, word);
            word.back() = '1';
            if (check(word)) backtrack(n + 1, word);
            word.pop_back();
        } else {
            word.push_back(P[n]);
            if (check(word)) backtrack(n + 1, word);
            word.pop_back();
        }
    }
}

void solve(int caseNum) {
    ans = 0;
    backtrack(0, "");
    cout << "Case " << caseNum << ": " << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    int caseNum = 1;
    while (getline(cin, line)) {
        if (line == "0") break;
        P = line.substr(line.find(' ') + 1);
        solve(caseNum++);
    }

    return 0;
}
