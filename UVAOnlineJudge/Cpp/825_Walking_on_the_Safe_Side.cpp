#include <iostream>
#include <unordered_set>
#include <sstream>

using namespace std;

struct pair_hash {
    size_t operator()(const pair<int, int>& p) const {
        return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
    }
};

unordered_set<pair<int,int>,pair_hash> blocked;

int W,N;
int ans;

bool check(int i, int j)
{
    return !blocked.count(make_pair(i,j));
}

void backtracking(int i, int j)
{
    if (i == W && j == N)
    {
        ans+=1;
    }else if (i<=W && j<=N){
        int pos [2][2] = {{i+1,j},{i,j+1}};
        
        for (int k = 0; k<2; k++)
        {
            if (check(pos[k][0], pos[k][1]))
            {
                backtracking(pos[k][0], pos[k][1]);
            }
        }
    }
}

int main()
{
    int T;
    cin>>T;
    for (int t = 0; t<T; t++)
    {
        string empty;
        getline(cin,empty);
        cin>>W>>N;
        cin.ignore();

        blocked = unordered_set<pair<int,int>, pair_hash>();
        ans = 0;
        for (int w = 0; w<W; w++)
        {
            string line;
            getline(cin, line);
            stringstream ss(line);

            int nline;
            ss>>nline;
            int wline;
            while(ss>>wline)
            {
                blocked.insert(make_pair(nline, wline));
            }
        }
        backtracking(1,1);
        cout<<ans<<endl;
        if (t<T-1)
        {
            cout<<endl;
        }
    }
    return 0;
}