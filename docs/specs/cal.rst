.. doctest docs/specs/cal.rst
.. include:: /../docs/shared/include/defs.rst

.. _presto.specs.cal:

=============================
The Calendar plugin in Presto
=============================

Presto extends the standard :mod:`lino_xl.lib.cal` plugin
:mod:`lino_presto.lib.cal`.

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *

Teams
=====

A team is a group of workers responsible for a given activity.
Each order must have a team (:attr:`lino_xl.lib.orders.Order.team`).

.. class:: Room

    .. attribute:: event_type
    .. attribute:: guest_role

>>> print(rt.models.cal.Room._meta.verbose_name)
Team

>>> rt.show(cal.Rooms)
============== ================== ================== =====================
 Designation    Designation (de)   Designation (fr)   Calendar entry type
-------------- ------------------ ------------------ ---------------------
 Garden works   Gartenarbeiten     Garden works       Garden works
 House works    House works        House works        Home help
 Office         Büro               Bureau
============== ================== ================== =====================
<BLANKLINE>

