# -*- coding: utf8 -*-
import fileinput
import json
import os

result = {}
for line in fileinput.input():
    arr = line.split('[')
    s = arr[1].split(']')
    for i in s[0].split(' '):
        i = i.strip()
        d = i.split('/')[0].split('.')
        if len(d) > 1:
            result[i.strip()] = 1

print json.dumps(sorted(result.keys()))
