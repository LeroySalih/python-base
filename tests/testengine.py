class TestAssertionError(Exception):
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

class TestResult:

    def __init__(self, name, status, expected, actual):
        self.name= name
        self.status = status
        self.expected = str(expected) 
        self.actual = str(actual) 

    
    def toDict (self):
        return {"name" : self.name, "status": self.status, "expected": self.expected, "actual": self.actual}


class TestEngine:
    
    def __init__(self, label):
        self.success = 0
        self.fails = 0
        self.results = []
        self.label = label
    
    def setUp(self):
        print("\n\nRunning Tests.\n")

    def tearDown(self):
        print("Done.")

    def assertEqual(self, expected, actual, msg):
        if expected != actual:
            raise TestAssertionError(expected, actual)

    def runTest(self, fn):
        try:
            fn()
            self.results.append(TestResult( fn.__name__, "passed", None, None).toDict())

        except TestAssertionError as err:
            #print(type(err), err)
            self.results.append(TestResult(
                fn.__name__, 
                "failed", 
                err.expected, 
                err.actual).toDict())
            
    def run(self):
        pass
        