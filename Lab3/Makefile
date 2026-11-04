main: main.o fibonacci.o
	cc main.o fibonacci.o -o main

main.o: main.c
	cc -Iheaders -c main.c -o main.o

fibonacci: fibonacci.o
	cc fibonacci.o -o fibonacci

fibonacci.o: fibonacci.c
	cc -Iheaders -c fibonacci.c -o fibonacci.o 

clean:
	rm *.o

run: main
	./main
