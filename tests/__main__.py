from subprocess import run

import os,sys,inspect
import requests 
import json 

from testengine import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from starter import *


print("*" * 20)
print(f"Testing Pod {os.environ['POD_ID']} for {os.environ['APP_EMAIL']}")
print("*" * 20)

    
class StarterTestEngine (TestEngine):

    def __init__(self, label):
        super().__init__(label);

    def test_output_is_correct(self): 
        user_input="Hello World"    
        result = run(["python", "starter.py"], input=b"Hello World\n", capture_output=True)
        
        expected = b'Enter a word.The first letter is H\nThe last letter is d\n'
        self.assertEqual(expected,  result.stdout, "\nExpected:\n{0}\nReceived:\n{1}".format(expected, result.stdout))

    def test_def_is_correct(self):
        result = mySum(4, 5)
        self.assertEqual( 9, mySum(4, 5), "\nExpected: 9.\nReceived:{0}".format(result))

    def run(self):

        self.runTest(self.test_output_is_correct)
        self.runTest(self.test_def_is_correct)

        return self.results



"""
    def test_variable_exists(self):
        self.assertNotEqual(pupil_age, None, "The variable pupil age has not been declared.")    
        
    def test_fn(self):
        self.assertEqual(mySum(5, 4), 9)
            
    def test_output(self):
        result = run(["python", "main.py"], input=b"12\n", capture_output=True)
        self.assertEqual(result.stdout, b"Enter your age:You are 12 years old\n", "Returned: {0}".format(result.stdout))        
"""

def textReset():
    print(u"\u001b[0m", end="")

def textGreen():
    print(u"\u001b[32m", end="")

def textRed():
    print(u"\u001b[31m", end="")

def agg(results):
    success = 0
    fails = 0

    for result in results:
        
        if result['status'] == 'passed':
            success = success + 1
        else:
            fails = fails + 1

    
    return success, fails

def createTestSuite (engine):
    
    results = engine.run()

    #Posting Results to Server
    params = {
        "email": os.environ["APP_EMAIL"],
        "podId": os.environ["POD_ID"],
        "results" : json.dumps(results)
    }

    result = requests.post(
        "https://3000-ab155182-05d4-4bf5-b47e-2b757b153877.ws-eu01.gitpod.io/api/test-result",
        # "https://python-code-test-server.herokuapp.com/api/test-result",
        data=params
        )

    
    print(f"Running tests for {engine.label}")
    for result in results:
        print("")
        if (result["status"] == "passed"):
            textGreen()
            print(u'\u2714', end=" ")
            textReset()
            print("{0}......Passed".format(result["name"]))
        else:
            textRed()
            print(u'\u2718', end=" ")
            textReset()
            print ("{0}.....Failed".format(result["name"]))
            print("\tExpected")
            print("\t========")
            print("\t", result['expected'])
            print("")
        
            print("\tActual")
            print("\t========")
            print("\t", result['actual'])
        
        textReset()

    success, fail = agg(results)

    progress = ((2 / (float(success) + float(fail))) ) * 100.0

    print(f"{engine.label} is {progress} % complete.")
    print("")
    print("")

if __name__ == "__main__":

    engine = StarterTestEngine("Starter")
    createTestSuite(engine)

    engine = StarterTestEngine("Step1")
    createTestSuite(engine)
