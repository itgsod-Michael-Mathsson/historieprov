 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml

with open("bernadotte.yaml") as f:
    family = yaml.load(f)



def printall(person):
    yield person["name"], person["death"]

    if "consort" in person:
        for i in printall(person["consort"]):
            yield i
    if "mistress" in person:
        for i in printall(person["mistress"]):
            yield i
    if "barn" in person:
        for i in range(len(person["barn"])):
            for j in printall(person["barn"][i]):
                yield j



for i in printall(family["bernadotte"]):
    if i[1] is None:
        print i[0]