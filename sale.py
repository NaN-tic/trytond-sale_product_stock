# This file is part of the sale_product_stock module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction


__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    @classmethod
    def __setup__(cls):
        super(Sale, cls).__setup__()
        cls._error_messages.update({
                'not_enough_stock': 'There are not enough stock of product '
                    '"%s" at this moment at the warehouse to make this sale.',
                })

    @classmethod
    def quote(cls, sales):
        super(Sale, cls).quote(sales)
        cls.enough_stock(sales)

    @classmethod
    def enough_stock(cls, sales):
        Product = Pool().get('product.product')
        for sale in sales:
            locations = [sale.warehouse.id]
            for line in sale.lines:
                with Transaction().set_context(locations=locations):
                    quantity = Product.get_quantity([line.product], 'quantity')
                if not quantity or quantity[line.product.id] < line.quantity:
                    cls.raise_user_warning('not_enough_stock_%s' % line.id,
                        'not_enough_stock', line.product.name)
