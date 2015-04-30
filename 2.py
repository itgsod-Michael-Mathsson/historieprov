 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml

with open("bernadotte.yaml") as f:
    persons = []
    current = []
    for i in f.readlines():
        if "name" in i:
            persons.append(current)
            current = []
        current.append(i.lstrip(" ").strip("\r\n"))

alive = []
for i in range(len(persons)):
    for j in persons[i]:
        if "death" in j:
            if "1" not in j and "2" not in j:
                alive.append(persons[i][0].strip("name: "))
print alive








