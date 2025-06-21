#include <iostream>

using namespace std;

int A[1001];

long long dp [1002][1002][2];
int game = 1;

long long phi(int i, int j) {
    long long ans = 0;
    if (dp[i][j][1] == game)
    {
        ans = dp[i][j][0];
    }else{
        if (i == j)
        {
            ans = 0;
        }else if (i+1 == j && A[i] < A[j]){
            ans = A[j]-A[i];
        }
        else if (i+1 == j && A[i] >= A[j]){
            ans = A[i]-A[j];
        }else{
            if ((j-i+1)%2 == 0)
            {
                ans = max(A[i]+phi(i+1, j), A[j]+phi(i, j-1));
            }else{
                if (A[i] >= A[j])
                {
                    ans = -1*A[i]+phi(i+1, j);
                }else{
                    ans = -1*A[j]+phi(i, j-1);
                }
            }
        }
        dp[i][j][0] = ans;
        dp[i][j][1] = game;
    }
    return ans;
}


int main(){
    int n;
    cin>>n;
    game = 1;
    for (int i = 0; i<1002; i++)
    {
        for (int j = 0; j<1002; j++)
        {
            dp[i][j][0] = 0;
            dp[i][j][1] = 0;
        }
    }
    while (n != 0)
    {
        for (int i = 0; i<n; i++)
        {
            cin>>A[i];
        }
        cout<<"In game "<<game<<", the greedy strategy might lose by as many as "<<phi(0, n-1)<<" points."<<endl;
        cin>>n;
        game++;
    }
    return 0;
}

/*


}*/