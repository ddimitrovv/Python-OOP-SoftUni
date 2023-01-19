from unittest import TestCase, main

from project1.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.username = "Celena"
        self.level = 50
        self.health = 120
        self.damage = 100
        self.hero = Hero(self.username, self.level, self.health, self.damage)
        self.enemy = Hero('Mannon', self.level, self.health, self.damage)

    def test_hero_init__should_return_correct_obj(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_battle__enemy_equal_to_hero__expected_exception(self):
        with self.assertRaises(Exception) as error:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_hero_battle__self_health_less_or_equal_to_zero__expected_exception(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_hero_battle__enemy_health_less_or_equal_to_zero__expected_exception(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(error.exception))

    def test_hero_battle__both_heroes_health_less_or_equal_to_zero__expected_to_return_draw(self):
        actual = self.hero.battle(self.enemy)
        self.assertEqual('Draw', actual)

    def test_hero_battle__enemy_health_less_or_equal_to_zero__expected_to_return_hero_win(self):
        self.enemy.damage = 1
        actual = self.hero.battle(self.enemy)
        self.assertEqual('You win', actual)

    def test_hero_battle__enemy_health_less_or_equal_to_zero__expected_hero_level_to_be_increased(self):
        self.enemy.damage = 1
        self.hero.battle(self.enemy)
        self.assertEqual(self.level + 1, self.hero.level)

    def test_hero_battle__enemy_health_less_or_equal_to_zero__expected_hero_health_to_be_increased(self):
        self.enemy.damage = 1
        self.hero.battle(self.enemy)
        self.assertEqual(self.health + 5 - (self.enemy.damage * self.enemy.level), self.hero.health)

    def test_hero_battle__enemy_health_less_or_equal_to_zero__expected_hero_damage_to_be_increased(self):
        self.enemy.damage = 1
        self.hero.battle(self.enemy)
        self.assertEqual(self.damage + 5, self.hero.damage)

    def test_hero_battle__hero_health_less_or_equal_to_zero__expected_to_return_enemy_win(self):
        self.hero.damage = 1
        actual = self.hero.battle(self.enemy)
        self.assertEqual('You lose', actual)

    def test_hero_battle__hero_health_less_or_equal_to_zero__expected_enemy_level_to_be_increased(self):
        self.hero.damage = 1
        self.hero.battle(self.enemy)
        self.assertEqual(self.level + 1, self.enemy.level)

    def test_hero_battle__hero_health_less_or_equal_to_zero__expected_enemy_health_to_be_increased(self):
        self.hero.damage = 1
        self.hero.battle(self.enemy)
        self.assertEqual((self.health + 5 - (self.hero.damage * self.hero.level)), self.enemy.health)

    def test_hero_battle__hero_health_less_or_equal_to_zero__expected_enemy_damage_to_be_increased(self):
        self.enemy.damage = 1
        self.hero.battle(self.enemy)
        self.assertEqual(self.damage + 5, self.hero.damage)

    def test_hero_str__expected_correct_string(self):
        expected_str = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        actual = self.hero.__str__()
        self.assertEqual(expected_str, actual)


if __name__ == "__main__":
    main()
