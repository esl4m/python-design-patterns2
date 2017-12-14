class Publisher:
    def __init__(self):
        # MAke it un-inheritable
        pass

    def register(self):
        # OVERRIDE
        pass

    def unregister(self):
        # OVERRIDE
        pass

    def notify_all(self):
        # OVERRIDE
        pass


class TechForum(Publisher):
    def __init__(self):
        self._listOfUsers = []
        self.postname = None

    def register(self, userObj):
        if userObj not in self._listOfUsers:
            self._listOfUsers.append(userObj)

    def unregister(self, userObj):
        self._listOfUsers.remove(userObj)

    def notify_all(self):
        for objects in self._listOfUsers:
            objects.notify(self.postname)

    def write_new_post(self, postname):
        # User writes a post.
        self.postname = postname
        # When submits the post is published and notification is sent to all
        self.notify_all()


class Subscriber:
    def __init__(self):
        # make it un-inheritable
        pass

    def notify(self):
        # OVERRIDE
        pass


class User1(Subscriber):
    def notify(self,postname):
        print('User1 notified of a new post %s' % postname)


class User2(Subscriber):
    def notify(self, postname):
        print('User2 notified of a new post %s' % postname)


class SisterSites(Subscriber):
    def __init__(self):
        self._sisterWebsites = ["Site1", "Site2", "Site3"]

    def notify(self, postname):
        for site in self._sisterWebsites:
            # Send updates by any means
            print("Sent notification to site: %s" % site)


if __name__ == "__main__":
    techForum = TechForum()
    user1 = User1()
    user2 = User2()
    sites = SisterSites()

    techForum.register(user1)
    techForum.register(user2)
    techForum.register(sites)

    techForum.write_new_post("Observer Pattern in Python")

    techForum.unregister(user2)

    techForum.write_new_post("MVC Pattern in Python")
