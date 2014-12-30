import unittest
from donkus import parser
import importlib

importlib.reload(parser)

class Test_parser_tests(unittest.TestCase):
    
    def test_peek(self):
        result = parser.peek([('noun', 'bear'), ('verb', 'eat')])
        self.assertEqual('noun', 'noun')


    def test_match(self):
        word_list = [('verb', 'kill'),
                     ('stop', 'the'),
                     ('noun', 'princess')]
        result = parser.match(word_list, 'verb')
        
        self.assertEqual(('verb', 'kill'), result)


    def test_not_match(self):
        word_list = [('stop', 'the'),
                     ('noun', 'princess'),
                     ('verb', 'kill')]
        result = parser.match(word_list, 'verb')
        
        self.assertEqual(None, result)


    def test_skipping_words(self):
        word_list = [('stop', 'the'),
                     ('noun', 'princess')]
        parser.skip(word_list, 'stop')

        self.assertEqual([('noun', 'princess')], word_list)


    def test_parse_subject(self):
        word_list = [('stop', 'the'),
                     ('noun', 'princess')]
        result = parser.parse_subject(word_list)

        self.assertEqual(('noun', 'princess'), result)


    def test_parse_verb(self):
        word_list = [('verb', 'kill')]
        result = parser.parse_verb(word_list)

        self.assertEqual(('verb', 'kill'), result)


    def test_parse_object(self):
        word_list = [('stop', 'the'),
                     ('noun', 'bear')]
        result = parser.parse_object(word_list)

        self.assertEqual(('noun', 'bear'), result)

    def test_parse_number(self):
        word_list = [('number', 10),
                     ('noun', 'princesses'),
                     ('verb', 'ate'),
                     ('number', 11),
                     ('noun', 'crumbcakes')]
        result = parser.parse_number(word_list)

        self.assertEqual(('number', 10), result)

        parser.skip(word_list, 'noun')
        parser.skip(word_list, 'verb')

        result = parser.parse_number(word_list)

        self.assertEqual(('number', 11), result)

    def test_parse_sentence(self):
        word_list = [('stop', 'the'),
                     ('noun', 'bear'),
                     ('verb', 'ate'),
                     ('stop', 'the'),
                     ('noun', 'princess')]
        parsed_sentence = parser.parse_sentence(word_list)

        expected_sentence = parser.Sentence(('noun', 'bear'), 
                                            ('verb', 'ate'),
                                            ('noun', 'princess'))

        # the sentences' dictionaries are equal
        self.assertDictEqual(expected_sentence.__dict__, parsed_sentence.__dict__)

    def test_parse_error(self):
        word_list = [('stop', 'the'),
                     ('noun', 'bear')]

        self.assertRaises(parser.ParserError, parser.parse_verb, (word_list))

    def test_badly_formed_sentence_does_not_blow_up(self):
        word_list = [('stop', 'the'),
                     ('noun', 'bear'),
                     ('noun', 'princess'),
                     ('stop', 'the'),
                     ('verb', 'ran')]

        result = parser.parse_sentence(word_list)

        self.assertEqual(None, result)

if __name__ == '__main__':
    unittest.main(exit=False)
