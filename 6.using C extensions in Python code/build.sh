gcc -fpic --shared $(python3-config --includes) greetmodule.c -o greet.abi3.so
