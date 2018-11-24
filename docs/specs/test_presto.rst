.. _lino.tested.presto:

==================================
Miscellaneous tests in Lino Presto
==================================


>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *

Test whether the bootstrap3 user interface works:

>>> url = '/bs3/products/Products'
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print res.status_code
200

