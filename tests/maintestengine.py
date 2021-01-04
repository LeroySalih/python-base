from testengine import *
from subprocess import run

from main import *

class MainTestEngine (TestEngine):

    def __init__(self, label):
        super().__init__(label);

    def test_output_is_correct(self): 
        user_input="Hello World"    
        result = run(["python", "main.py"], input=b"Hello World\n", capture_output=True)
        
        expected = b'Enter a message.The first letter is H.\nThe last letter is d.\n'
        self.assertEqual(expected,  result.stdout, "\nExpected:\n{0}\nReceived:\n{1}".format(expected, result.stdout))

    def test_def_exists(self):
        self.assertDefExists("mySum")
    
    def test_def_is_correct(self):
        result = mySum(4, 5)
        self.assertEqual( 9, mySum(4, 5), "\nExpected: 9.\nReceived:{0}".format(result))

    def getTests(self):
        return [self.test_output_is_correct, 
                self.test_def_exists, 
                self.test_def_is_correct]