# -*- coding: UTF-8 -*-
# Copyright 2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino_xl.lib.orders.models import *
from lino.api import _


class Missions(Orders):
    label = _("Missions")


class Contracts(Orders):
    label = _("Contracts")


# OrderAreas.clear()
# add = OrderAreas.add_item
# add('100', _("Missions"), 'default', 'orders.Missions')
# add('200', _("Contracts"), 'contracts', 'orders.Contracts')


