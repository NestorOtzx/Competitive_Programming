#include <iostream>
#include <iomanip>
#include <math.h>
#include <string>
using namespace std;

#define EPS 10e-6
#define INF 10e9;

int t, n;
double c [20][2];

double margin(double mid){
    double bestTime = INF;
    for (int i = 0; i<n-1; i++)
    {
        bestTime = min(bestTime, (mid/c[i][0]) + ((t-mid)/c[i][1]));
        //cout<<"best time: "<<bestTime<< " calc:"<<(mid/c[i][0]) + ((t-mid)/c[i][1])<<endl;
    }
    double cheaterT = (mid/c[n-1][0]) + ((t-mid)/c[n-1][1]);
    return bestTime-cheaterT;
}

double solve(double l, double r)
{
    while (abs(l-r) >= EPS)
    {
        
        double trd = (r-l)/3;
        double lmid = l+trd;
        double rmid = r-trd;
        double mlmid = margin(lmid);
        double mrmid = margin(rmid);
        //cout<<"l:"<<l<<"r:"<<r<<"| lmid:"<<lmid<<" rmid:"<<rmid << "| mlmid: " <<mlmid <<" mrmid: "<<mrmid<<endl;
        if (mlmid <= mrmid)
        {
            l = lmid;
        }else{  
            r = rmid;
        }
    }
    return r;
}

int main()
{
    while (cin>>t)
    {
        cin>>n;
        for (int i = 0; i<n; i++)
        {
            cin>>c[i][0]>>c[i][1];
        }
        double r = solve(0, t);
        int time = round(margin(r)*3600);
        if (time >= 0)
        {
            cout<<fixed<<setprecision(2)<<"The cheater can win by "<<time<<" seconds with r = "<<r<<"km and k = "<<t-r<<"km."<<endl;
        }else{
            cout<<"The cheater cannot win."<<endl;
        }
    }


    return 0;
}