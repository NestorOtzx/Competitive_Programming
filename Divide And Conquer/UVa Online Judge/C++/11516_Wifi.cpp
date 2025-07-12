#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

int N,M;
vector<int> H;
const double EPS=1e-6;

double dround(double n){
    double res=n-floor(n);
    double ans=0;
    if(res<0.25) ans=floor(n);
    else if(res<0.75) ans=floor(n)+0.5;
    else ans=floor(n)+1.0;
    return ans;
}

int count(double mid){
    double curr=H[0];
    int cnt=1;
    for(int i=1;i<M;++i){
        if(H[i]-curr>mid){
            curr=H[i];
            cnt++;
        }
    }
    return cnt;
}

double phi(){
    double low=0.0,high=2.0*H.back(),mid;
    while(high-low>EPS){
        mid=(low+high)/2.0;
        if(count(mid)>N) low=mid;
        else high=mid;
    }
    return dround(mid/2.0);
}

void solve(){
    double ans=0;
    if(N<M) ans=phi();
    cout<<fixed<<setprecision(1)<<ans<<'\n';
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin>>T;
    for(int t=0;t<T;++t){
        cin>>N>>M;
        H.clear();
        H.resize(M);
        for(int i=0;i<M;++i){
            cin>>H[i];
        }
        sort(H.begin(),H.end());
        solve();
    }
    return 0;
}
