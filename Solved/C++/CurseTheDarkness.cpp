#include <iostream>
#include <math.h>
using namespace std;

double square(double a){
	return a * a;
}

int main(void)
{
	int tc,n,canLight;
	double ux,uy,cx,cy;
	cin>>tc;

	while(tc--)
	{
		cin>>ux>>uy;
		cin>>n;
		canLight=0;
		for (int j = 0; j < n; ++j)
		{
			cin>>cx>>cy;

			double d=sqrt(square(ux-cx) + square(uy-cy));
			if (d<=8.0000000)
			{
				canLight++;
			}
		}

		if (canLight!=0)
		{
			cout<<"light a candle\n";
		}
		else
		{
			cout<<"curse the darkness\n";
		}
	}
	return 0;
}