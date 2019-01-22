.. include:: /../../book/docs/shared/include/defs.rst

.. _lino.tested.presto:
.. _presto.specs.overview:

========
Overview
========

.. include:: /../../book/docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *



Some vocabulary
===============

================ ================================
English          German
================ ================================
Furniture        Möbel
Used furniture   Gebrauchtmöbel
Renovation       Renovierungsarbeiten
Bicycle studio   Fahrradwerkstatt
Furniture store  Möbellager
Garden services  Gartenarbeiten
Home help        Haushaltshilfe
Small repair     Kleinreparaturen im Haushalt
Laundry service  Wäschedienst (Waschbären)
Transport        Transport
Moving           Umzüge
Delivery note    Lieferschein
================ ================================


- Managed as contracts : Garden contracts, Home help
- Managed as delivery notes  : Bicycle, Transport, Small repair, Moving, Furniture store, Renovation




Don't read me
=============


Test whether the bootstrap3 user interface works:

>>> url = '/bs3/products/Products'
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print res.status_code
200

