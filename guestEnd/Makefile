obj-m += hash.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
run:
	make all
	sudo insmod hash.ko
	sudo rmmod hash
	dmesg
daemon:	
	sudo insmod hash.ko
	sudo rmmod hash
