dvcp:dvcp.o
	afl-clang-fast -O1 -g dvcp.c -o dvcp
dvcp.o:dvcp.c
	cc -c dvcp.c -o dvcp.o
clean:
	rm *.o
