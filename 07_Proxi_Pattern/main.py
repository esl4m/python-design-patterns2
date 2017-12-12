import time


class Manager(object):
    def work(self):
        pass

    def talk(self):
        pass


class SalesManager(Manager):
    def work(self):
        print("Sales Manager working...")

    def talk(self):
        print("Sales Manager ready to talk")


class Proxy(Manager):
    def __init__(self):
        self.busy = 'Yes'
        self.sales = None

    def work(self):
        print("Proxy checking for Sales Manager availability")

        if self.busy == 'Yes':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")


if __name__ == '__main__':
    p = Proxy()
    p.work()
