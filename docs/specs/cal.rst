.. doctest docs/specs/cal.rst
.. include:: /../docs/shared/include/defs.rst

.. _presto.specs.cal:

=============================
The Calendar plugin in Presto
=============================

Presto extends the standard :mod:`lino_xl.lib.cal` plugin
:mod:`lino_presto.lib.cal`.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *

Teams
=====

A team is a group of workers responsible for a given activity.

The team of an order is defined by its journal. You can have a same team for
different journals, but you cannot have several teams for one journal.

Lino Presto injects a field :attr:`lino_xl.lib.ledger.Journal.room`.

.. class:: Room

    .. attribute:: event_type
    .. attribute:: guest_role
    .. attribute:: invoicing_area

>>> print(rt.models.cal.Room._meta.verbose_name)
Team

>>> rt.show(cal.Rooms)
============= ================== ================== =====================
 Designation   Designation (de)   Designation (fr)   Calendar entry type
------------- ------------------ ------------------ ---------------------
 Garden        Garten             Garden             Outside work
 Moves         Umzüge             Moves              Outside work
 Renovation    Renovierung        Renovation         Inside work
 Home help     Haushaltshilfe     Home help          Inside work
 Home care     Heimpflege         Home care          Inside work
 Office        Büro               Bureau             Office work
============= ================== ================== =====================
<BLANKLINE>

