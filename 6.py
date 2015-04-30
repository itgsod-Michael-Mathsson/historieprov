 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml

with open("bernadotte.yaml") as f:
    consorts = []

    people = 1
    for i in f.readlines():
        if "consort" in i:
            people = 0
        if people == 0:
            if "name" in i:
                consorts.append(i.strip("name: ").strip("\r\n"))
                people = 1

for i in consorts:
    print i