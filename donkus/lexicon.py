import sys
import types
import re

current_module = sys.modules[__name__]

directions = ["north","south","east","west","up","down"]
verbs = ["go", "kill", "eat"]

def scan(str):
    input = str.split()
    results = []
    for word in input:
        tuple = probe_for(word)
        results.append(tuple)

    return results


def probe_for(word):
    #harvest all module-level lists
    word_lists = {key:value for (key,value) in  [ (a,current_module.__dict__.get(a)) for a in dir(current_module) if isinstance(current_module.__dict__.get(a), type([]))]}
    for key, list in word_lists.items():
        found = get_first(filter_by_value(list, word))
        if found:
            key = re.sub('s$', '', key) #depluralize - todo: use an inflection
            return (key, word)

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def filter_by_value(seq, value):
   for s in seq:
       if s == value: 
           yield s

def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default
