#! /bin/bash
gen  ()
{ head -c 1024K -z </dev/urandom | hexdump -C -n 1024 > keyfile && sed -i '$d' keyfile  
 } 

hasher () 
{ cat "keyfile" | while read -r line; do
    printf %s "$line" | sha512sum | cut -f1 -d' '

    done; }

gen && hasher keyfile | tee key && rm keyfile

exit
