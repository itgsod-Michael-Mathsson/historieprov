 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml


names = []

with open("bernadotte.yaml") as f:
    for i in f.readlines():
        if "name" in i:
            names.append(i.lstrip("name: ").strip("\r\n"))


print names
