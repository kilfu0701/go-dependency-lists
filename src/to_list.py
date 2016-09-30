# -*- coding: utf8 -*-
import fileinput
import json

result = {}
for line in fileinput.input():
    arr = line.strip().split('"')
    if len(arr) == 3:
        result[arr[1]] = 1

print json.dumps(sorted(result.keys()))
