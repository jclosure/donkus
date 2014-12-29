# define this module's errors
class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        # these are tuples, e.g. ('noun', 'bear')
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj = obj[1]

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

### MODULE-LEVEL FUNCTIONS

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    sentence = Sentence(subj, verb, obj)
    return sentence

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word_type = peek(word_list)
           
    if next_word_type == 'noun':
        return match(word_list, 'noun')
    elif next_word_type == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a noun or verb next.")

def parse_verb(word_list):
    skip(word_list, 'stop')
    next_word_type = peek(word_list)

    if next_word_type == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word_type = peek(word_list)

    if next_word_type == 'noun':
        return match(word_list, 'noun')
    elif next_word_type == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")



####### HELPERS ############

def peek(word_list):
    if word_list:
        word = word_list[0] #grab first word tuple
        word_type = word[0] #grab the type from the first slot
        return word_type
    else:
        return None
    
# match has a front remove side-effect on word_list
def match(word_list, expected_type):
    if word_list:
        word = word_list.pop(0)
        word_type = word[0]
        if word_type == expected_type:
            return word
        else:
            return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

