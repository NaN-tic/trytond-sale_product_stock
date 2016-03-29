# This file is part of the sale_product_stock module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['Sale']
PRODUCT_TYPES = ['goods']


class Sale:
    __metaclass__ = PoolMeta
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
    def check_enough_stock(cls):
        if Transaction().context.get('without_warning'):
            return False
        return True

    @classmethod
    def get_enough_stock_qty(cls):
        Config = Pool().get('sale.configuration')
        return Config(1).enough_stock_qty or 'quantity'

    @classmethod
    def enough_stock(cls, sales):
        if not cls.check_enough_stock():
            return

        Product = Pool().get('product.product')

        # get all products
        products = []
        for sale in sales:
            locations = [sale.warehouse.id]
            for line in sale.lines:
                if not line.product or line.product.type not in PRODUCT_TYPES:
                    continue
                if line.product not in products:
                    products.append(line.product)

        # get quantity
        with Transaction().set_context(locations=locations):
            quantities = Product.get_quantity(
                products,
                cls.get_enough_stock_qty(),
                )

        # check enough stock
        for sale in sales:
            for line in sale.lines:
                if line.product and line.product.id in quantities:
                    qty = quantities[line.product.id]
                    if qty < line.quantity:
                        cls.raise_user_warning('not_enough_stock_%s' % line.id,
                            'not_enough_stock', line.product.name)
                    # update quantities
                    quantities[line.product.id] = qty - line.quantity
