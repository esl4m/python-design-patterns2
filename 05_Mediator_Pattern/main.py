import time


class TC:
    def __init__(self):
        self._tm = tm
        self._bProblem = 0

    def setup(self):
        print("Setting up the Test")
        time.sleep(1)
        self._tm.prepare_reporting()

    def execute(self):
        if not self._bProblem:
            print("Executing the test")
            time.sleep(1)
        else:
            print("Problem in setup. Test not executed.")

    def tear_down(self):
        if not self._bProblem:
            print("Tearing down")
            time.sleep(1)
            self._tm.publish_report()
        else:
            print("Test not executed. No tear down required.")

    def setTM(self, tm):
        self._tm = tm

    def set_problem(self, value):
        self._bProblem = value


class Reporter:
    def __init__(self):
        self._tm = None

    def prepare(self):
        print("Reporter Class is preparing to report the results")
        time.sleep(1)

    def report(self):
        print("Reporting the results of Test")
        time.sleep(1)

    def setTM(self, tm):
        self._tm = tm


class DB:
    def __init__(self):
        self._tm = None

    def insert(self):
        print("Inserting the execution begin status in the Database")
        time.sleep(1)
        # Following code is to simulate a communication from DB to TC
        import random
        if random.randrange(1, 4) == 3:
            return -1

    def update(self):
        print("Updating the test results in Database")
        time.sleep(1)

    def setTM(self, tm):
        self._tm = tm


class TestManager:
    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepare_reporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.set_problem(1)
            self._reporter.prepare()

    def set_reporter(self, reporter):
        self._reporter = reporter

    def setDB(self, db):
        self._db = db

    def publish_report(self):
        self._db.update()
        rvalue = self._reporter.report()

    def setTC(self,tc):
        self._tc = tc


if __name__ == '__main__':
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.set_reporter(reporter)
    tm.setDB(db)

    reporter.setTM(tm)
    db.setTM(tm)

    # For simplification we are looping on the same test.
    # Practically, it could be about various unique test classes and their objects
    while 1:
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tear_down()
