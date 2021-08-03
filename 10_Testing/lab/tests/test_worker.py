from lab.project.worker import Worker
import unittest
from unittest import TestCase


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_worker_is_initialised_correct(self):
        # Arrange and Act
        # worker = Worker("Test", 100, 10)
        worker = self.worker
        # Assert
        self.assertEqual('Test', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_energy_increase_after_rest(self):
        # Arrange
        # worker = Worker('Test', 100, 10)
        worker = self.worker
        self.assertEqual(10, worker.energy)
        # Act
        worker.rest()
        # Assert
        self.assertEqual(11, worker.energy)

    def test_worker_worked_with_negative_energy_raises(self):
        # Arrange
        worker = Worker('Test', 100, 0)

        # Act
        with self.assertRaises(Exception) as ex:
            worker.work()
        # Assertion
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_is_increased_after_work(self):
        # Arrange
        # worker = Worker('Test', 100, 10)
        worker = self.worker
        self.assertEqual(0, worker.money)
        # Act
        worker.work()
        # Assert
        self.assertEqual(100, worker.money)

    def test_worker_energy_is_decrease_after_working(self):
        # Arrange
        # worker = Worker('Test', 100, 10)
        worker = self.worker
        self.assertEqual(10, worker.energy)
        # Act
        worker.work()
        # Assert
        self.assertEqual(9, worker.energy)

    def test_ger_info(self):
        # Arrange
        # worker = Worker('Test', 100, 10)
        worker = self.worker
        # Act
        actual_result = worker.get_info()
        expected_result = "Test has saved 0 money."
        # Assert
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
