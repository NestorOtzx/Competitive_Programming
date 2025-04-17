#include <iostream>

//it can be improved reducing the tab space, but i dont want to think too much about it.

using namespace std;

int P[1000];
int L[1000];



int dp[1001][6002];


int solve(int N, int ML)
{
    for (int n = N; n >= 0; n--)
    {
        for (int ml = 0; ml <= ML; ml++)
        {
            if (n == N)
            {
                dp[n][ml] = 0;
            }else{
                if (ml-P[n] >= 0)
                {
                    dp[n][ml] = max(1+dp[n+1][min(ml-P[n], L[n])], dp[n+1][ml]);
                }else{
                    dp[n][ml] = dp[n+1][ml];
                }
            }
        }
    }
    /*
    for (int n = N; n >= 0; n--)
    {
        for (int ml = 0; ml <= ML; ml++)
        {
            cout<<dp[n][ml]<<",";
        }
        cout<<endl;
    }*/


    return dp[0][6001];
}

int main()
{
    int N;
    while (cin>>N && N != 0)
    {
        for (int n = 0; n<N; n++)
        {
            cin>>P[n]>>L[n];
        }
        int ans = solve(N, 6002);
        cout<<ans<<endl;
    }

    return 0;
}