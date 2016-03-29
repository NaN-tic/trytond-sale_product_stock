#This file is part sale_product_stock module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Configuration']


class Configuration:
    __metaclass__ = PoolMeta
    __name__ = 'sale.configuration'
    enough_stock_qty = fields.Property(fields.Selection([
        ('quantity', 'Quantity'),
        ('forecast_quantity', 'Forecast Quantity'),
        ], 'Quantity Stock',
        help='Manage Stock is Product Quantity or Product Forecast Quantity'))
