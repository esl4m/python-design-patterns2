class Person:
    def __init__(self):
        self.name = None
        self.gender = None

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender


class Male(Person):
    def __init__(self, name):
        print("Hello Mr." + name)


class Female(Person):
    def __init__(self, name):
        print("Hello Miss." + name)


class Factory:
    def get_person(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.get_person("Chetan", "M")
