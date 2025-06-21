#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <tuple>
using namespace std;

int N;
int T;
int s[20];

int dp1[21][100001];

int phitab(int MSUM)
{
    for (int t = T; t>= 0; t-- )
    {
        for (int sum = MSUM; sum >= 0; sum--)
        {
            if (t == T)
            {
                dp1[t][sum] = sum;
            }else{
                if (s[t] + sum <= N)
                {
                    dp1[t][sum] = max(dp1[t+1][sum+s[t]], dp1[t+1][sum]);
                }else{
                    
                    dp1[t][sum] = dp1[t+1][sum];
                }
            }
        }
    }
    return dp1[0][0];
}

bool ans = false;

void backtrack(int t, int sum, int m){
    if (sum == 0 && !ans)
    {
        for (int i = 0; i<t; i++)
        {
            if (m & (1<<i))
            {
                cout<<s[i]<<" ";
            }
        }
        ans = true;
    }else if (!ans && t < T){
        if (sum-s[t] >= 0){
            int nm = m | 1<<t;
            backtrack(t+1, sum-s[t], nm);
            backtrack(t+1, sum, m);
        }else{
            backtrack(t+1, sum, m);
        }
    }

}



int main(){
    string data;
    getline(cin, data);
    while (data.length() > 0)
    {
        stringstream ss(data);
        ss>>N;
        ss>>T;
        ans = false;
        for (int t = 0; t<T; t++){
            ss>>s[t];
        }
        int msum = phitab(T*N);
        backtrack(0, msum, 0);
        cout<<"sum:"<<msum<<endl;
        getline(cin, data);
    }

    return 0;
}