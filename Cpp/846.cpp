#include <iostream>

int solve(int x, int y, int step)
{
    int ans = 0;
    if (x >= y)
    {
        ans = 0;
    }else if (x+step >= y){
        ans = 1;
    }else{
        ans = 2+solve(x+step, y-step, step+1);
    }
    return ans;
}


int main()
{
    int N;
    std::cin>>N;
    for (int n = 0; n < N ; n++)
    {
        int x, y;
        std::cin>>x>>y;
        std::cout<<solve(x,y,1)<<std::endl;
    }
    return 0;
}