main: main.o fibonacci.o
	cc main.o fibonacci.o -o main

main.o: main.c
	cc -Iheaders -c main.c -o main.o

fibonacci: fibonacci.o
	cc fibonacci.o -o fibonacci

fibonacci.o: fibonacci.c
	cc -Iheaders -c fibonacci.c -o fibonacci.o 

test-output: main
	@echo "Running integration test..."
	@./main > output.txt
	@grep -Fq "55" output.txt || (echo "Failed: 55 not found" && exit 1)
	@grep -Fq "1.618034" output.txt || (echo "Failed: 1.618034 not found" && exit 1)
	@echo "Output tests passed!"
	@rm -f output.txt

test: test_main.o fibonacci.o
	cc test_main.o fibonacci.o -o test_runner
	./test_runner

test_main.o: test_main.c
	cc -Iheaders -c test_main.c -o test_main.o

clean:
	rm *.o main test_runner

run: main
	./main
