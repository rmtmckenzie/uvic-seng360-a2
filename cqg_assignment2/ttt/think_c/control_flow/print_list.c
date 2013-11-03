/*
Trivial use.

Print a list of integers on a line.
May be the most common trivial use example of this operator.
*/


#include <stdlib.h>

#include <stdio.h>

int main(int argc, char* argv[])
{
	for (int i = 0; i < 5; i++)
		printf("%d%c",i, i == 4 ? '\n' : ' ');

	return 0;
}
