#include <iostream>

int main(void)
{
    int n;
    while(std::cin>>n && n>0)
    {
        int sum = 0;
        while(n>= 10)
        {
            sum += n%10;
            n = n/10;
            if (n < 10)
            {
                n = sum+n;
                sum = 0;
            }
        }
        std::cout<<n<<"\n";
    }
    return 0;
}