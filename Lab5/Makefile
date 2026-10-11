fuzz:
	mkdir -p build
	afl-clang-fast -O1 -g -o build/fuzz_target \
	  fuzz/fuzz_target.c src/parser.c
