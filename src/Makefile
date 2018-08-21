# Makefile

# includes
incdir = .

# compilers/flags
compiler = g++ 
flags = -O2 -std=c++11 -I $(incdir)

# the program
run-example: example.cc
		$(compiler) $(flags) $< -o $@ -lz

clean:
		rm -f  run-example


