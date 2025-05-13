#include <iostream>

using namespace std;

long long trees[1000001];

int main(){
    long long N, M;
    while (cin>>N>>M)
    {
        for (long long n = 0; n<N; n++)
        {
            cin>>trees[n];
        }

        long long l = 0, h = 2000000000;
        while (l+1<h)
        {
            long long mid = l+((h-l)>>1);
            long long wood = 0;
            for (int n = 0; n<N; n++)
            {
                if (trees[n]>mid)
                {
                    wood+=trees[n]-mid;
                }
            }
            if (wood>=M)
            {
                l = mid;
            }else{
                h = mid;
            }
        }
        cout<<l<<endl;
    }
    return 0;
}