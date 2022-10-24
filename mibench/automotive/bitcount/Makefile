FILE = bitcnt_1.c bitcnt_2.c bitcnt_3.c bitcnt_4.c bitcnts.c bitfiles.c bitstrng.c bstr_i.c

bitcnts: ${FILE} Makefile
	aarch64-linux-gnu-gcc -static ${FILE} -O3 -o bitcnts # change the compiler to gcc-aarch64-linux-gnu

clean:
	rm -rf bitcnts output*
