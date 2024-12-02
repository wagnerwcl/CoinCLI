import unittest

from main import Expense

class TestExpense(unittest.TestCase):

    def set_up(self):
        self.expense = Expense

    def test_add(self):
        result = self.expense.add("Garrafa de Agua", 45.50)
        self.assertEqual(result, "Garrafa de Agua", 45.50)

if __name__ == '__main__':
    unittest.main()