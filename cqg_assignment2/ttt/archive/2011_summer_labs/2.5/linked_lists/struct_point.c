#include <stdio.h>

struct point {
	int x;
	int y;
};

void shiftpoint(struct point *p, int delta)
{
	p->x += delta;
	p->y += delta;
}

int contains(struct point p, struct point p0, struct point p1)
{
	if (p.x >=  p0.x && p.x <= p1.x && p.y >=  p0.y && p.y <= p1.y)
		return 1;
	else
		return 0;
}

int main()
{
	struct point a0 = {0,0};
	struct point a1 = {5,5};
	struct point a2 = {1,2};
	int i;

	for (i = 0; i < 5; i++) {
		shiftpoint(&a2,1);
		printf("%d\n", contains(a2,a0,a1));
	}

	return 0;	
}
