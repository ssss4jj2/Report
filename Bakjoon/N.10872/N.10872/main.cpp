#include <stdio.h>

int main()
{
	int i;
	int j=1;
	printf("���� �Է� : ");
	scanf_s("%d",&i);

	for (int k = 1; k <= i; k++)
	{
		j = (k * j);
	}
	return j;
	printf("�������=", j);
}