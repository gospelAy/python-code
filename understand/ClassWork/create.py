class Person:
    def __init__(self, name, age, day):
        self._name = name
        self._age = age
        self._day = day

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_day(self):
        return self._day

    def set_day(self, day):
        self._day = day
        
