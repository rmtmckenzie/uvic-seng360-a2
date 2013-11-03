/* Minimal: as little as possible beyond the operator itself.

This question is one of 160 generated from a template.
In the template, the condition is
	$x $operator $y
where $x and $y are single digit
and $operator is any relational or logical operator.
*/


#include <stdlib.h>

#include <stdio.h>

int main(int argc, char* argv[])
{
	printf("%s\n", -2 < -2 ? "a" : "b");

	return 0;
}
