#include<iostream>
#include<conio.h>

using namespace std;
int main()
{
    int i,j,n,k;
    cout<<"Enter number of rows : ";
    cin>>n;
    //Displaying pattern
    for(i=n; i>=1; i--)
    {
        for(j=1; j<=i; j++)
        {
            cout<<j<<" ";
        }
        for(k=1; k<(n-i+1)*2-2; k++)
        {
            cout<<"* ";
        }
        cout<<"\n";
    }
    getch();
    return 0;
}
