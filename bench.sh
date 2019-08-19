#!/usr/bin/env bash

for dir in $(find . -type d -name '[!.]*' -maxdepth 1); do
    cd "$dir"
    ./build
    cd ..
    echo "Language $dir"
    time ("$dir/fac" > number)
    if ! diff -q expected number &> /dev/null; then
        echo "FAIL"
        exit 1
    else
        echo "PASS"
    fi
done
