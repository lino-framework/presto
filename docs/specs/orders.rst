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
============ ============================= ======== ==========
 Start date   Client                        Remark   Workflow
------------ ----------------------------- -------- ----------
 14/01/2017   DEMEULENAERE Dorothée (121)            **Done**
 12/01/2017   COLLARD Charlotte (117)                **Done**
 11/01/2017   CHARLIER Ulrike (118)                  **Done**
 11/01/2017   CHANTRAINE Marc (119)                  **Done**
 11/01/2017   BRECHT Bernd (176)                     **Done**
 09/01/2017   BASTIAENSEN Laurent (116)              **Done**
 08/01/2017   AUSDEMWALD Alfons (115)                **Done**
 07/01/2017   ARENS Annette (113)                    **Done**
 06/01/2017   ARENS Andreas (112)                    **Done**
 04/01/2017   ALTENBERG Hans (114)                   **Done**
 03/01/2017   Maria (242)                            **Done**
 03/01/2017   Ahmed (241)                            **Done**
============ ============================= ======== ==========
<BLANKLINE>


>>> rt.show(orders.OrderStates, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
======= ============ =========== ==========
 value   name         text        Editable
------- ------------ ----------- ----------
 10      draft        Waiting     Yes
 20      active       Active      Yes
 30      urgent       Urgent      Yes
 40      registered   Done        No
 50      cancelled    Cancelled   No
======= ============ =========== ==========
<BLANKLINE>

>>> rt.show(ledger.VoucherTypes, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
=========================== ====== ========================================= ======================================================
 value                       name   text                                      Model
--------------------------- ------ ----------------------------------------- ------------------------------------------------------
 orders.OrdersByJournal             Order (orders.OrdersByJournal)            <class 'lino_xl.lib.orders.models.Order'>
 orders.TraOrdersByJournal          Order (orders.TraOrdersByJournal)         <class 'lino_xl.lib.orders.models.Order'>
 sales.InvoicesByJournal            Sales invoice (sales.InvoicesByJournal)   <class 'lino_xl.lib.sales.models.VatProductInvoice'>
 vat.InvoicesByJournal              Invoice (vat.InvoicesByJournal)           <class 'lino_xl.lib.vat.models.VatAccountInvoice'>
=========================== ====== ========================================= ======================================================
<BLANKLINE>

>>> ledger.VoucherTypes.get_for_model(orders.Order)
