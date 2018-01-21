// QuadSelection.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	int x, y;

	scanf("%d%d", &x, &y);

	if (x > 0)
	{
		if (y > 0)
		{
			printf("1");
		}
		else
		{
			printf("4");
		}
	}
	else
	{
		if (y > 0)
		{
			printf("2");
		}
		else
		{
			printf("3");
		}
	}

	//system("pause");
    return 0;
}
