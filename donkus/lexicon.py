import sys, types, re

current_module = sys.modules[__name__]

directions = ["north","south","east","west","up","down"]
verbs = ["go", "kill", "eat"]
stops = ["the", "in", "of"]
nouns = "bear princess".split()

def scan(str):
    input = str.split()
    results = []
    for word in input:
        num = convert_number(word)
        if num:
            results.append(('number', num))
        else:
            tuple = probe_for(word)
            if tuple:
                results.append(tuple)
            else:
                results.append(('error', word))
        
    return results

def probe_for(word):
    #harvest all module-level lists
    word_lists = {key:value for (key,value) in  [(a,current_module.__dict__.get(a)) for a in dir(current_module) if isinstance(current_module.__dict__.get(a), type([]))]}
    for key, list in word_lists.items():
        found = get_first(filter_by_value(list, word))
        if found:
            key = re.sub('s$', '', key) #depluralize - todo: use an inflection
            return (key, found)

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def filter_by_value(seq, value):
   for s in seq:
       if s.lower() == value.lower(): 
           yield s #generator

def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default
