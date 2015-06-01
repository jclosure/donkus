import collections

try:
    # Python 2.7+
    basestring
except NameError:
    # Python 3.3+
    basestring = str

#@staticmethod
def todict(obj):
    """ 
    Recursively convert a Python object graph to sequences (lists)
    and mappings (dicts) of primitives (bool, int, float, string, ...)
    """
    if isinstance(obj, basestring):
        return obj 
    elif isinstance(obj, dict):
        return dict((key, todict(val)) for key, val in obj.items())
    elif isinstance(obj, collections.Iterable):
        return [todict(val) for val in obj]
    elif hasattr(obj, '__dict__'):
        return todict(vars(obj))
    elif hasattr(obj, '__slots__'):
        return todict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
        return obj
