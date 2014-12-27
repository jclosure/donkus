
directions = ["north","south","east","west","up","down"]

def scan(str):
    input = str.split()
    results = []
    for word in input:
        match = get_first(filterbyvalue(directions, word))
        if match:
            results.append(('direction', match))
    return results

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def filterbyvalue(seq, value):
   for s in seq:
       if s == value: 
           yield s

def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default
