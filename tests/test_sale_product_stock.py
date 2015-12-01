# This file is part of the sale_product_stock module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleProductStockTestCase(ModuleTestCase):
    'Test Sale Product Stock module'
    module = 'sale_product_stock'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleProductStockTestCase))
    return suite