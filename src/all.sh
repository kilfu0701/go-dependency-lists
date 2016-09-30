#!/bin/bash

#arr=( "v1.0.0" "v1.1.0" "v1.2.0" "v1.3" "v1.4" "v1.4.1" "v1.4.2" )
for i in $@
do
    git checkout "$i"
    find . -name "*.go" | xargs awk -f ~/Desktop/github/go-dependency-lists/src/find_import.awk | python ~/Desktop/github/go-dependency-lists/src/to_list.py | python -mjson.tool > "$i.json"
done
