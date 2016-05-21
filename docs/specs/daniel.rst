.. _presto.specs.daniel:

======================================
Lino Presto à la Daniel : introduction
======================================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_daniel
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_presto.projects.daniel.settings.doctests')
    >>> from lino.api.doctest import *

The "Daniel" variant of Lino Presto is to be used in a center for
ambulant consultations by phychologists.

The code name for this is :mod:`lino_presto.projects.daniel`.

>>> settings.SETTINGS_MODULE
'lino_presto.projects.daniel.settings.doctests'

They use *time tracking* from :ref:`noi`, but unlike :ref:`noi` they
have no notion of *tickets*.

>>> dd.plugins.clocking
lino_noi.lib.clocking

>>> dd.is_installed('tickets')
False

When a psychologist starts a session, they want to assign it to a
"dossier".  A dossier is either a single person, or a family or
household, or a *therapeutic group*. 
A dossier is their central database object.
Many statistical reports are based on these dossiers.

Their dossiers correspond to Lino's notion of partners.

>>> print(dd.plugins.clocking.ticket_model)
<class 'lino_presto.lib.contacts.models.Partner'>

>>> print(settings.SITE.project_model)
<class 'lino_presto.lib.contacts.models.Partner'>

There might be (it is not yet decided) a differetiation between
"partner" and "dossier": a same partner can have more than one dossier
within the years. But currently they simply create the same partner a
second time (and add a field which connects them).

