#! /bin/bash
while getopts s:n: flag
do
    case "${flag}" in
        n) name=${OPTARG};;
        s) size=${OPTARG};;
          esac
done
gen  ()
{ head -c "$size" -z </dev/urandom > /tmp/keyfile && sed -i '$d' /tmp/keyfile  
 } 

hasher () 
{ cat /tmp/keyfile | while read -r line; do
    printf %s "$line" | sha512sum  | cut -f1 -d' '

    done; }

gen && hasher keyfile | tee "$name" &&  truncate --size "$size" "$name"

exit
