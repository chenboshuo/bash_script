#!/bin/sh
ping www.baidu.com -i 30|awk -F "[=]|[ ]" '/bytes from/{print NR "\t" $11/1000 "\t" strftime("%c",systime())} '
