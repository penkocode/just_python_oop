from project.hero import Hero

from unittest import TestCase, main


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Mushu', 100, 200, 300)
        self.enemy = Hero('Toto', 100, 200, 300)
        self.power_hero = Hero('Power', 1000, 200000, 3000)

    def test_init_method_assertion(self):
        self.assertEqual('Mushu', self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(200, self.hero.health)
        self.assertEqual(300, self.hero.damage)

    def test_battle_with_yourself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_no_hero_health_left(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_no_enemy_health_left(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        res = self.hero.battle(self.enemy)
        self.assertEqual('Draw', res)

    def test_battle_win(self):
        res = self.power_hero.battle(self.enemy)
        self.assertEqual('You win', res)
        self.assertEqual(self.power_hero.health, 170005)
        self.assertEqual(self.power_hero.damage, 3005)
        self.assertEqual(self.power_hero.level, 1001)
        self.assertEqual(self.enemy.health, -2999800)
        self.assertEqual(self.enemy.damage, 300)
        self.assertEqual(self.enemy.level, 100)

    def test_battle_lose(self):
        res = self.enemy.battle(self.power_hero)
        self.assertEqual('You lose', res)
        self.assertEqual(self.power_hero.health, 170005)
        self.assertEqual(self.power_hero.damage, 3005)
        self.assertEqual(self.power_hero.level, 1001)
        self.assertEqual(self.enemy.health, -2999800)
        self.assertEqual(self.enemy.damage, 300)
        self.assertEqual(self.enemy.level, 100)

    def test_string_method(self):
        self.assertEqual(f"Hero Mushu: 100 lvl\n"f"Health: 200\n"f"Damage: 300\n", str(self.hero))


if __name__ == "__main__":
    main()
