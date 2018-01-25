// PizzaCrust.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <cmath>

using namespace std;

int main()
{
	int r, c;
	double pi = 3.1415926535897;

	cin >> r >> c;

	double pizza = pi*r*r;
	double cheese = pi*(r - c)*(r - c);

	double perc = 100 * cheese / pizza;

	printf("%.6f\n", perc);

	//system("pause");
    return 0;
}
