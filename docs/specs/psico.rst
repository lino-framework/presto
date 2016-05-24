.. _presto.specs.psico:

=============================
Lino Psico : a first overview
=============================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_psico
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_presto.projects.psico.settings.doctests')
    >>> from lino.api.doctest import *

**Lino Psico** (from Italian *psicologo*, psychologist) is a variant
of :ref:`presto` designed to be used in a center for
`sociopsychological
<https://en.wikipedia.org/wiki/Social_psychology>`_ consultations.

All :ref:`psico` application have a :xfile:`settings.py` module which
inherits from :mod:`lino_presto.projects.psico.settings`.

>>> settings.SETTINGS_MODULE
'lino_presto.projects.psico.settings.doctests'

Lino Psico uses *time tracking* from :ref:`noi`, but unlike :ref:`noi`
it does not have the notion of *tickets*.

>>> dd.plugins.clocking
lino_noi.lib.clocking

>>> dd.is_installed('tickets')
False

When a psychologist starts a session, they don't specify a *ticket*
but a *partner*.  

>>> print(dd.plugins.clocking.ticket_model)
<class 'lino_presto.lib.contacts.models.Partner'>

In Lino Psico, the partner is the central database object.  Many
statistical reports are based on attributes of partners.  

>>> print(settings.SITE.project_model)
<class 'lino_presto.lib.contacts.models.Partner'>

A partner is either a single person, a family, a household, or a group
of otherwise non-related partners having a same problem (called a
*therapeutic group*).

There might be (it is not yet decided) a differetiation between
"partner" and "dossier": a same partner can have more than one dossier
within the years. Currently they simply create the same partner a
second time (and add a field which connects them).

