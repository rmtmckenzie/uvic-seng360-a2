/* Trivial use: plausibly useful, but showing how the operator might
be useful outweighs any considerations for actual use.

{\it Compare} rewritten as a nested conditional expression.
*/


#include <stdlib.h>

#include <stdio.h>

int main(int argc, char* argv[])
{

	int x = 1;
	int y = 1;

	int n = x < y ? -1 : x == y ? 0 : 1;

	printf("%d\n", n);

	return 0;
}
