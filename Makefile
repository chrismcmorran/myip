all:
	pip3 install cython
	cython --embed myip.py -o myip.c
	cc $(shell pkg-config --libs --cflags python3) -O3 myip.c -o myip

install:
	cp myip /usr/local/bin/myip

clean:
	rm myip.c
	rm myip
