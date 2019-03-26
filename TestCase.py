class TestCase():
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

    def setUp(self):
        pass

    def tearDown(self):
        pass

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def testMethod(self):
        self.log += "testMethod "

    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log += "tearDown "
