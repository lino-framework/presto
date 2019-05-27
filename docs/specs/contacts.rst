.. doctest docs/specs/contacts.rst
.. include:: /../docs/shared/include/tested.rst

.. _presto.specs.contacts:

========
Contacts
========

.. currentmodule:: lino_presto.lib.contacts

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *



.. class:: Worker

    The Django model which represents a worker.

    A MTI child of :class:`Person`


20190527
========


>>> ba = rt.models.contacts.Workers.detail_action
>>> ut = rt.login('rolf').get_user().user_type

>>> ba.get_view_permission(ut)
True

