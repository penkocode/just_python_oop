from project_01_wild_cat_zoo.worker import Worker


class Keeper(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
