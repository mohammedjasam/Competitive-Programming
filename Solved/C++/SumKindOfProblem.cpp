// PizzaCrust.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <cmath>

using namespace std;

int sum(int N)
{
	int sum;
	sum = (N + 1) * N / 2;
	return sum;
}

int sumEven(int N)
{
	int sum;
	sum = ((N + 1) * N) ;
	return sum;
}

int sumOdd(int n)
{
	int sum;
	sum = n*n;
	return sum;
}

int main()
{
	int t;
	cin >> t;
	int k, n;

	for (int i = 0; i < t; i++)
	{
		cin >> k >> n;
		cout << k << " " << sum(n) << " " << sumOdd(n) << " " << sumEven(n) << endl;
	}
	//system("pause");
    return 0;
}
