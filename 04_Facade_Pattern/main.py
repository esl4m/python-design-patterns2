import time


class TC1:
    def run(self):
        print("###### In Test 1 ######")
        time.sleep(1)
        print("Setting up")

        time.sleep(1)
        print("Running test")

        time.sleep(1)
        print("Tearing down")

        time.sleep(1)
        print("Test Finished\n")


class TC2:
    def run(self):
        print("###### In Test 2 ######")
        time.sleep(1)
        print("Setting up")

        time.sleep(1)
        print("Running test")

        time.sleep(1)
        print("Tearing down")

        time.sleep(1)
        print("Test Finished\n")


class TC3:
    def run(self):
        print("###### In Test 3 ######")
        time.sleep(1)
        print("Setting up")

        time.sleep(1)
        print("Running test")

        time.sleep(1)
        print("Tearing down")

        time.sleep(1)
        print("Test Finished\n")


# Facade
class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()

    def run_all(self):
        self.tc1.run()
        self.tc2.run()
        self.tc3.run()


# Client
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.run_all()
