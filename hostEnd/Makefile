obj-m += hash.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
run:
	sudo rmmod hash
	make all
	sudo insmod hash.ko
	dmesg
