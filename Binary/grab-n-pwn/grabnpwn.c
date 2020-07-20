#include <stdio.h>
#include <stdlib.h>

void
func1()
{
	char buffer[100];
	gets(buffer);
	fflush(stdin);

	printf(buffer);
	fflush(stdout);
}

void
func2()
{
	char buffer[100];
	gets(buffer);
	fflush(stdin);

	printf("%s\n", buffer);
	fflush(stdout);
}

int
main()
{	
	func1();
	func2();

	return 0;
}
