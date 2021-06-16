#include <unistd.h>
#include <sys/ioctl.h>
//#include <stdio.h>

int main()
{
	setuid(1000);
	setgid(1000);
	system("/bin/bash");
	//printf("ID: %d\n", geteuid());
	//execve("/bin/sh", NULL, NULL);
}

