.. _presto.specs.teams:

===================
Teams in Lino Psico
===================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_teams
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_presto.projects.psico.settings.doctests')
    >>> from lino.api.doctest import *



>>> rt.show(teams.Teams)
============= ================== ==================
 Designation   Designation (de)   Designation (fr)
------------- ------------------ ------------------
 Eupen
 St.Vith
============= ================== ==================
<BLANKLINE>
