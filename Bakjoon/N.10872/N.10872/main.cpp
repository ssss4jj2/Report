#include <stdio.h>

int main()
{
	int i;
	int j=1;
	printf("숫자 입력 : ");
	scanf_s("%d",&i);

	for (int k = 1; k <= i; k++)
	{
		j = (k * j);
	}
	return j;
	printf("결과값은=", j);
}