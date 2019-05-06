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


>>> rt.show(orders.Orders, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
============ ============================= ======== ================
 Start date   Client                        Remark   Workflow
------------ ----------------------------- -------- ----------------
 14/01/2017   DEMEULENAERE Dorothée (121)            **Registered**
 12/01/2017   COLLARD Charlotte (117)                **Registered**
 11/01/2017   CHARLIER Ulrike (118)                  **Registered**
 11/01/2017   CHANTRAINE Marc (119)                  **Registered**
 11/01/2017   BRECHT Bernd (176)                     **Registered**
 09/01/2017   BASTIAENSEN Laurent (116)              **Registered**
 08/01/2017   AUSDEMWALD Alfons (115)                **Registered**
 07/01/2017   ARENS Annette (113)                    **Registered**
 06/01/2017   ARENS Andreas (112)                    **Registered**
 04/01/2017   ALTENBERG Hans (114)                   **Registered**
 03/01/2017   Maria (242)                            **Registered**
 03/01/2017   Ahmed (241)                            **Registered**
============ ============================= ======== ================
<BLANKLINE>

