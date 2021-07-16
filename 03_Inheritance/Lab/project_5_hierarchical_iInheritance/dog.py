from Lab.project_5_hierarchical_iInheritance.animal import Animal


class Dog(Animal):
    def bark(self):
        return 'barking...'


d = Dog()
print(d.eat())
