class Animal:

    def __init__(self, name):
        self.name = name


    def __str__(self):
        return 'This is an animal'

    def __str__(self):
        return 'This is not an animal'

animal = Animal('Thais')

print(animal)