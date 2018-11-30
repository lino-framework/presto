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

>>> dd.plugins.courses._verbose_name

>>> rt.show(courses.CourseAreas)

>>> rt.show(courses.Courses)
