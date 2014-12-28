from nose import *
from nose.tools import *
from donkus import lexicon
import importlib


importlib.reload(lexicon)

def setup():
    pass

def teardown():
    pass

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])


    

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go')
                          ('verb', 'kill')
                          ('verb', 'eat')])



#for executing tests in repl
run()