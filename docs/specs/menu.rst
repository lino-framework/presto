.. doctest docs/specs/menu.rst
.. include:: /../docs/shared/include/defs.rst

.. _presto.specs.menu:

========
The menu
========

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *


>>> rt.login('robin').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP
Not yet tested because menu items for calendar entries aren't ready


>>> rt.show(ledger.JournalGroups)
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

