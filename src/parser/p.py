# -*- coding: utf-8 -*-
import json
import re

# python p.py | python -mjson.tool > pkg_lists.json

result = {}
with open('d.txt', 'r')  as f:
    lines = f.readlines()

    r = re.compile(r'.*(github.com/.*\))')
    for line in lines:
        m = r.match(line)

        if m:
            url = m.group(1).split(')')[0]
            url = url.split('#')[0]
            if url[-1] == '/':
                url = url[:len(url) - 1]

            result[url] = 1

lists = sorted(result.keys())
print json.dumps(lists)
