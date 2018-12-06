# -*- coding: UTF-8 -*-
# Copyright 2013-2018 Rumma & Ko Ltd

from __future__ import unicode_literals

from lino_xl.lib.products.models import *


class ProductDetail(ProductDetail):
    # Make the sales_price visible
    main = """
    id cat sales_price vat_class delivery_unit
    name
    description
    """