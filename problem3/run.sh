#!/bin/bash

t=$(date +\%Y\%m\%d\%H\%M\%S)
#echo "$t"

cd log
touch $t.log
cd ..

python3 crawl.py >> log/$t.log 2>&1

exit 0
