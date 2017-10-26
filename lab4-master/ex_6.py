# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import Timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique


path = 'data_light.json'



with open(path) as f:
    data = json.load(f)



@print_result
def f1(arg):
    return sorted(unique(field(arg, 'job-name'), ignore_case=True),
             key=lambda item: item.lower())


@print_result
def f2(arg):
    pass


@print_result
def f3(arg):
    pass


@print_result
def f4(arg):
    pass


with Timer():
    f4(f3(f2(f1(data))))
