from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 99.9)

    def test_init_assign(self):
        fuel = 100
        hp = 99.9
        default_fuel_consumption = 1.25

        self.assertEqual(fuel, self.vehicle.fuel)
        self.assertEqual(hp, self.vehicle.horse_power)
        self.assertEqual(fuel, self.vehicle.capacity)
        self.assertEqual(default_fuel_consumption, self.vehicle.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(20)
        self.assertEqual(75, self.vehicle.fuel)

    def test_drive_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.fuel -= 50
        self.vehicle.refuel(10)
        self.assertEqual(60, self.vehicle.fuel)

    def test_reel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_string_represent(self):
        self.assertEqual("The vehicle has 99.9 horse power with 100 fuel left and 1.25 fuel consumption",
                         str(self.vehicle))

        if __name__ == '__main__':
            main()
