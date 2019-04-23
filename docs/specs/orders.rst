.. doctest docs/specs/orders.rst
.. include:: /../docs/shared/include/defs.rst

.. _presto.specs.orders:

=========
Orders
=========

Orders in Presto are implemented using the :mod:`lino_xl.lib.orders`
plugin.

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *

>>> print(dd.plugins.orders.verbose_name)
Orders

>>> #rt.show(orders.Orders)


>>> rt.show('ledger.JournalGroups')
======= =========== ===========
 value   name        text
------- ----------- -----------
 05      orders      Orders
 10      sales       Sales
 20      purchases   Purchases
 30      wages       Wages
 40      financial   Financial
 50      vat         VAT
======= =========== ===========
<BLANKLINE>
