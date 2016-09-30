# -*- coding: utf8 -*-
import fileinput
import json
import os
result = {}

glide_fn = 'glide.yaml'

if os.path.isfile(glide_fn):
    with open(glide_fn, 'r') as f:
        lines = f.readlines()
        for line in lines:
            arr = line.strip().split('- package:')
            if len(arr) == 2:
                result[arr[1].strip()] = 1

for line in fileinput.input():
    arr = line.strip().split('"')
    if len(arr) == 3:
        result[arr[1]] = 1

print json.dumps(sorted(result.keys()))
