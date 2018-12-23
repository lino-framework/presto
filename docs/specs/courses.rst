.. doctest docs/specs/courses.rst
.. include:: /include/defs.rst

.. _presto.specs.courses:

=========
Contracts
=========

Contracts in Presto are implemented using the :mod:`lino_xl.lib.courses`
plugin.

.. include:: /include/tested.rst

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *

>>> print(dd.plugins.courses.verbose_name)
Contracts

>>> rt.show(courses.CourseAreas)
======= ========= ================== =========================
 value   name      text               Table
------- --------- ------------------ -------------------------
 10      default   Home help          courses.HomeContracts
 20      garden    Garden contracts   courses.GardenContracts
======= ========= ================== =========================
<BLANKLINE>

>>> rt.show(courses.Courses)
No data to display
