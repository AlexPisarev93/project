from unittest import TestCase, main
from utils.calculator import calculator


class Calculator(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Начали тесты")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Тесты закончили")

    def setUp(self) -> None:
        print("Тест начался")

    def tearDown(self) -> None:
        print("Тест закончен")

    def test_division(self):
        print(1)
        self.assertEqual(calculator(10, 5), 2)

    def test_str(self):
        print(2)
        self.assertEqual(calculator("20", "4"), 5)

    def test_zero(self):
        with self.assertRaises(ValueError) as err:
            calculator(12, 0)
        self.assertEqual("На ноль делить нельзя!!!", err.exception.args[0])


if __name__ == '__main__':
    main()