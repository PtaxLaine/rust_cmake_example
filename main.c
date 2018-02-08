#include <stdio.h>
#include <stdlib.h>

extern void foobar(void);

int main(void){
	printf("main.c:%d\n", __LINE__);
	fflush(stdout);
	foobar();
	printf("main.c:%d\n", __LINE__);
	return 0;
}
