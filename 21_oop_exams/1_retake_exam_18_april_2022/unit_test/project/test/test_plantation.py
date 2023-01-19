import os
from unittest import TestCase, main

from project.plantation import Plantation


class TestPlantation(TestCase):
    SIZE = 100

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init__expected_correct_result(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertDictEqual({}, self.plantation.plants)
        self.assertListEqual([], self.plantation.workers)

    def test_init__zero_size__expected_correct_obj(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertDictEqual({}, self.plantation.plants)
        self.assertListEqual([], self.plantation.workers)

    def test_init__with_invalid_size__expected_to_raise_value_error(self):
        size = -1
        expected = "Size must be positive number!"
        with self.assertRaises(ValueError) as error:
            self.plantation.size = size
        self.assertEqual(expected, str(error.exception))

    def test_hire_worker__worker_not_in_workers__expected_correct_result(self):
        worker = 'worker'
        actual = self.plantation.hire_worker(worker)
        expected = f"{worker} successfully hired."
        self.assertEqual(expected, actual)
        self.assertListEqual([worker], list(self.plantation.workers))
        self.assertDictEqual({}, self.plantation.plants)

    def test_hire_worker__worker_in_workers__expected_to_raise_value_error(self):
        worker = 'worker'
        self.plantation.hire_worker(worker)
        expected = "Worker already hired!"
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker(worker)
        self.assertEqual(expected, str(error.exception))
        self.assertListEqual([worker], list(self.plantation.workers))

    def test_len__without_plants__expected_0(self):
        actual = self.plantation.__len__()
        self.assertEqual(0, actual)

    def test_len__with_plants__expected_correct_result(self):
        self.plantation.hire_worker('worker')
        self.plantation.planting('worker', 'plant1')
        self.plantation.planting('worker', 'plant2')
        actual = self.plantation.__len__()
        self.assertEqual(2, actual)

    def test_planting__worker_not_in_plantation_expected_to_raise_value_error(self):
        worker = 'worker'
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, 'plant')
        expected = f"Worker with name {worker} is not hired!"
        self.assertEqual(expected, str(error.exception))
        self.assertDictEqual({}, dict(self.plantation.plants))
        self.assertListEqual([], list(self.plantation.workers))

    def test_planting__worker_in_plantation_first_plant__expected_correct(self):
        worker = 'worker'
        plant = 'plant'
        self.plantation.hire_worker(worker)
        actual = self.plantation.planting(worker, plant)
        expected = f"{worker} planted it's first {plant}."
        self.assertEqual(expected, actual)
        self.assertDictEqual({worker: [plant]}, dict(self.plantation.plants))
        self.assertListEqual([plant], list(self.plantation.plants[worker]))

    def test_planting__worker_in_plantation_not_first_plant__expected_correct(self):
        worker = 'worker'
        plant = 'plant'
        plant2 = 'plant2'
        expected = f"{worker} planted {plant2}."
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, plant)
        actual = self.plantation.planting(worker, plant2)
        self.assertEqual(expected, actual)
        self.assertDictEqual({worker: [plant, plant2]}, dict(self.plantation.plants))
        self.assertListEqual([plant, plant2], list(self.plantation.plants[worker]))

    def test_planting__not_enough_space__expected_to_raise_value_error(self):
        self.plantation.size = 1
        worker = 'worker'
        plant = 'plant'
        plant2 = 'plant2'
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, plant)
        expected = "The plantation is full!"
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, plant2)
        self.assertEqual(expected, str(error.exception))
        self.assertDictEqual({worker: [plant]}, dict(self.plantation.plants))

    def test_str__empty_plantation__expected_correct_result(self):
        expected = f"""Plantation size: {self.SIZE}\n"""
        self.assertEqual(expected, str(self.plantation))

    def test_str__plantation_with_worker_and_plants__expected_correct_result(self):
        worker = 'worker'
        plant = 'plant'
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, plant)
        expected = f"""Plantation size: {self.SIZE}
{worker}
{worker} planted: {plant}"""
        self.assertEqual(expected, str(self.plantation))

    def test_repr__plantation_without_worker_and_plants__expected_correct_result(self):
        expected = f"Plantation size: {self.SIZE}" + os.linesep + f'{os.linesep.join([])}'
        self.assertEqual(expected, str(self.plantation))

    def test_repr__with_workers__expected_correct_result(self):
        worker = 'worker'
        worker2 = 'worker2'
        worker3 = 'worker3'
        plant = 'plant'
        self.plantation.hire_worker(worker)
        self.plantation.hire_worker(worker2)
        self.plantation.hire_worker(worker3)
        self.plantation.planting(worker, plant)
        actual = repr(self.plantation)
        workers = [worker, worker2, worker3]
        result = ''
        result += f'Size: {self.SIZE}\n'
        result += f'Workers: {", ".join(workers)}'
        expected = result
        self.assertEqual(expected, actual)

    def test_repr__without_workers__expected_correct_result(self):
        actual = repr(self.plantation)
        workers = []
        result = ''
        result += f'Size: {self.SIZE}\n'
        result += f'Workers: {", ".join(workers)}'
        expected = result
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
