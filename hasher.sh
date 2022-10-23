#! /bin/zsh
cat "$@" | while read -r line; do
    printf %s "$line" | md5sum | grep -o '^\S\+' | cut -f1 -d ''
done
