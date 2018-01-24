// Herman.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdio.h>
#include <iostream>

using namespace std;

int sumOfDigits(int num)
{
	int sum = 0;

	while (num > 0)
	{
		int digit = num % 10;
		sum = sum + digit;
		num /= 10;
	}
	return sum;
}

int main()
{
	do
	{
		int N;

		cin >> N;

		if (N == 0)
		{
			break;
		}
		else
		{
			int i = 11;
			while (1)
			{
				if (sumOfDigits(N) == sumOfDigits(N*i))
				{
					cout << i << endl;
					break;
				}
				else
				{
					i++;
				}
			}
		}
	} while (1);


	//system("pause");
    return 0;
}
