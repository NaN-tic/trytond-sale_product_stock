#!/usr/bin/env python
# This file is part of the sale_product_stock module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_depends
import trytond.tests.test_tryton
import unittest


class SaleProductStockTestCase(unittest.TestCase):
    'Test Sale Product Stock module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_product_stock')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('sale_product_stock')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleProductStockTestCase))
    return suite
