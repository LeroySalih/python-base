import main

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

    def getTests (self):
        return []

    def runTest(self, fn):
        try:
            #run the test
            fn()

            #test didn't throw an exception, so OK.
            self.results.append(TestResult( fn.__name__, "passed", None, None).toDict())

        except TestAssertionError as err:
            #print(type(err), err)
            self.results.append(TestResult(
                fn.__name__, 
                "failed", 
                err.expected, 
                err.actual).toDict())

        except NameError as err:
            self.results.append(TestResult(
                fn.__name__, 
                "failed", 
                "Def not found", 
                "").toDict())

    # Run all tests rather than halting at the first fail.
    def run(self):
        for test in self.getTests():
            self.runTest(test)

        return self.results


    def assertDefExists (self, name):
        defs = dir(main)
        if not(name in defs):
            raise TestAssertionError(f"Expected to find def {name}", f"{name} not found.-")