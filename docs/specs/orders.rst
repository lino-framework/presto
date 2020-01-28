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

>>> with translation.override("en"):
...     print(dd.plugins.orders.verbose_name)
Orders

>>> rt.show(ledger.JournalGroups, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
======= =========== ============================
 value   name        text
------- ----------- ----------------------------
 05      orders      Orders
 10      sales       Sales
 20      purchases   Purchases
 30      wages       Wages
 40      financial   Financial
 50      vat         VAT
 60      misc        Miscellaneous transactions
======= =========== ============================


>>> rt.show(orders.Orders, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
============ ============================= ======== ============
 Start date   Client                        Remark   Workflow
------------ ----------------------------- -------- ------------
 14/01/2017   DEMEULENAERE Dorothée (121)            **Active**
 12/01/2017   COLLARD Charlotte (117)                **Active**
 11/01/2017   CHARLIER Ulrike (118)                  **Active**
 11/01/2017   CHANTRAINE Marc (119)                  **Active**
 11/01/2017   BRECHT Bernd (176)                     **Active**
 09/01/2017   BASTIAENSEN Laurent (116)              **Active**
 08/01/2017   AUSDEMWALD Alfons (115)                **Active**
 07/01/2017   ARENS Annette (113)                    **Active**
 06/01/2017   ARENS Andreas (112)                    **Active**
 04/01/2017   ALTENBERG Hans (114)                   **Active**
 03/01/2017   Maria (242)                            **Active**
 03/01/2017   Ahmed (241)                            **Active**
============ ============================= ======== ============
<BLANKLINE>


>>> rt.show(orders.OrderStates, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
======= ============ =========== =============
 value   name         text        Button text
------- ------------ ----------- -------------
 10      draft        Waiting
 20      registered   Active
 30      signed       Done
 40      cancelled    Cancelled
======= ============ =========== =============
<BLANKLINE>
