#include <iostream>

using namespace std;

#define MAXT 60*3*50+1
int dp[51][MAXT][2];

void solve(int * songs, int N, int T, int c)
{
    T = min(T, MAXT);
    for (int n = 0; n <= N; n++)
    {
        for (int t = 0; t <= T; t++)
        {
            if (n == 0)
            {
                dp[n][t][0] = 0;
                dp[n][t][1] = 0;
            }else{
                if (t-songs[n-1]>= 0)
                {
                    if (1+dp[n-1][t-songs[n-1]][1] > dp[n-1][t][1])
                    {
                        dp[n][t][0] = songs[n-1]+dp[n-1][t-songs[n-1]][0];
                        dp[n][t][1] = 1+dp[n-1][t-songs[n-1]][1];
                    }else if (1+dp[n-1][t-songs[n-1]][1] == dp[n-1][t][1])
                    {
                        if (songs[n-1]+dp[n-1][t-songs[n-1]][0] > dp[n-1][t][0])
                        {
                            dp[n][t][0] = songs[n-1]+dp[n-1][t-songs[n-1]][0];
                            dp[n][t][1] = 1+dp[n-1][t-songs[n-1]][1];
                        }else{
                            dp[n][t][0] = dp[n-1][t][0];
                            dp[n][t][1] = dp[n-1][t][1];
                        }
                    }
                    else{
                        dp[n][t][0] = dp[n-1][t][0];
                        dp[n][t][1] = dp[n-1][t][1];
                    }
                }else{
                    dp[n][t][0] = dp[n-1][t][0];
                    dp[n][t][1] = dp[n-1][t][1];
                }
            }
        }
    }
    cout<<"Case "<<c<<": "<<dp[N][T][1]+1<<" "<<dp[N][T][0]+678<<endl;
}

int main()
{
    int C;
    cin>>C;
    for (int c = 0; c<C; c++)
    {
        int N,T;
        cin>>N>>T;
        int * songs = new int[N];
        for (int n = 0; n<N; n++)
        {
            cin>>songs[n];
        }
        solve(songs, N, T-1,c+1);
    }
    return 0;
}