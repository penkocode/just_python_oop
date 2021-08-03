from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Alo', 'Beast', 'Zzzz')

    def test_init_create_all_attributes(self):
        self.assertEqual('Alo', self.mammal.name)
        self.assertEqual('Beast', self.mammal.type)
        self.assertEqual('Zzzz', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        res = self.mammal.make_sound()
        self.assertEqual('Alo makes Zzzz', res)

    def test_get_kingdom(self):
        res = self.mammal.get_kingdom()
        self.assertEqual('animals', res)

    def test_mammal_info(self):
        res = self.mammal.info()
        self.assertEqual('Alo is of type Beast', res)


if __name__ == '__main__':
    main()
