import unittest
from decimal import Decimal

from lib import App


class ReceiptUnitTest(unittest.TestCase):

    def test_input_one(self):
        receipt = App.run_simulation('samples/input#1.csv')
        self.assertEqual(len(receipt.purchases), 3)
        self.assertEqual(receipt.purchases[0].get_price(), Decimal('12.49'))
        self.assertEqual(receipt.purchases[1].get_price(), Decimal('16.49'))
        self.assertEqual(receipt.purchases[2].get_price(), Decimal('0.85'))
        self.assertEqual(receipt.get_sales_taxes(), Decimal('1.50'))
        self.assertEqual(receipt.get_total(), Decimal('29.83'))

    def test_input_two(self):
        receipt = App.run_simulation('samples/input#2.csv')
        self.assertEqual(len(receipt.purchases), 2)
        self.assertEqual(receipt.purchases[0].get_price(), Decimal('10.50'))
        self.assertEqual(receipt.purchases[1].get_price(), Decimal('54.65'))
        self.assertEqual(receipt.get_sales_taxes(), Decimal('7.65'))
        self.assertEqual(receipt.get_total(), Decimal('65.15'))

    def test_input_three(self):
        receipt = App.run_simulation('samples/input#3.csv')
        self.assertEqual(len(receipt.purchases), 4)
        self.assertEqual(receipt.purchases[0].get_price(), Decimal('32.19'))
        self.assertEqual(receipt.purchases[1].get_price(), Decimal('20.89'))
        self.assertEqual(receipt.purchases[2].get_price(), Decimal('9.75'))
        self.assertEqual(receipt.purchases[3].get_price(), Decimal('11.85'))
        self.assertEqual(receipt.get_sales_taxes(), Decimal('6.70'))
        self.assertEqual(receipt.get_total(), Decimal('74.68'))


if __name__ == '__main__':
    unittest.main()
