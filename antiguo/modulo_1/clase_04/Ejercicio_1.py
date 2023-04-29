import uuid

class Subject:

    def __init__(self, firstName='', age=0, id=uuid.uuid4()):
        self.firstName = firstName
        self.age = age
        self.id = id

    def disclose(self):
        if self.isAdult():
            return print(f'{self.firstName} has {self.age} years old and is adult with id = {self.id}')
        else:
            return print(f'{self.firstName} has {self.age} years old and is not adult with id = {self.id}')

    def isAdult(self):
        if self.age >= 18:
            return True
        else:
            return False

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

subject = Subject()

subject.setFirstName('Juanito')
subject.setAge(17)
subject.disclose()
