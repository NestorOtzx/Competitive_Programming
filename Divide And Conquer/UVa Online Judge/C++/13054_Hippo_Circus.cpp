#include <iostream>
#include <algorithm>

int N, H, ta, td;
int A[100001];

long long solve(int low, int high)
{
	long long ans = 0;
	if (low > high)
	{
		ans = 0;
	}else if (low == high)
	{
		ans = ta;
	}else if (low < high)
	{
		if (A[low] + A[high] >= H)
		{
			ans = ta + solve(low, high-1);
		}
		else if (A[low] + A[high] < H)
		{
			if (2*ta < td)
			{
				ans = 2*ta+solve(low+1, high-1);
			}
			else if (2*ta >= td){
				ans = td+solve(low+1, high-1);
			}
		}
	}
	return ans;
}

int main(){
    int casos;
    std::cin>>casos;
    for (int c = 1; c <= casos; c++)
    {
		
        std::cin>>N>>H>>ta>>td;
        
        for (int i = 0; i<N; i++)
        {
            std::cin>>A[i];
        }
		
		std::sort(A, A + N);
		
        long long ans = solve(0, N-1);
        std::cout<<"Case "<<c<<": "<<ans<<std::endl;
    }
    return 0;
}

