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

Workflow
========

>>> rt.show(cal.EntryStates)
====== ============ =============== ============= ================= ======== =================== =========
 Wert   name         Text            Button text   Gäste ausfüllen   Stabil   nicht blockierend   No auto
------ ------------ --------------- ------------- ----------------- -------- ------------------- ---------
 10     suggested    Vorschlag       ?             Ja                Nein     Nein                Nein
 20     draft        Geplant         ☐             Ja                Nein     Nein                Nein
 50     took_place   Stattgefunden   ☑             Nein              Ja       Nein                Nein
 60     missed       Missed          ☉             Nein              Ja       Nein                Ja
 70     cancelled    Abgesagt        ⚕             Nein              Ja       Ja                  Ja
====== ============ =============== ============= ================= ======== =================== =========
<BLANKLINE>

>>> rt.show(cal.GuestStates)
====== ========= ============== ================= =============
 Wert   name      Nachträglich   Text              Button text
------ --------- -------------- ----------------- -------------
 20     invited   Ja             Geplant           ☑
 50     needs     Ja             Sucht Ersatz      ⚕
 60     found     Nein           Ersatz gefunden   ☉
====== ========= ============== ================= =============
<BLANKLINE>


Replacement planning
====================

A worker announces that they need replacement for a deployment in the future.
You find the calendar entry, and in the :class:`GuestsByEntry` slave table,
Workflow column, change the presence state from "planned" to "needs replacement"

At any moment you can see the :class:`GuestsNeedingReplacement` table, which
shows all presences needing replacement.

>>> rt.login("robin").show(cal.GuestsNeedingReplacement)
============ ============ ============ ===================================================== ============================================== ===========
 Beginnt am   Beginnt um   Arbeiter     Kalendereintrag                                       Workflow                                       Bemerkung
------------ ------------ ------------ ----------------------------------------------------- ---------------------------------------------- -----------
 11.05.17     08:00:00     Herr Garry   `DERICUM Daniel (120) Eupen Einsatz 18  <Detail>`__   **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 26.08.17     08:00:00     Herr Garry   `DERICUM Daniel (120) Eupen Einsatz 33  <Detail>`__   **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 10.12.17     08:00:00     Herr Garry   `DERICUM Daniel (120) Eupen Einsatz 48  <Detail>`__   **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
============ ============ ============ ===================================================== ============================================== ===========
<BLANKLINE>

When this table is not empty, it causes a welcome message "You have 3 items in
Needing replacement".

In the workflow column you can click on "Find replacement" to specify another
worker who is going to replace the originally planned worker.


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

>>> rt.show(cal.Rooms, language="en")
================ ================== ================== =====================
 Designation      Designation (fr)   Designation (en)   Calendar entry type
---------------- ------------------ ------------------ ---------------------
 Garten           Garten             Garden             Outside work
 Umzüge           Umzüge             Moves              Outside work
 Renovierung      Renovierung        Renovation         Inside work
 Haushaltshilfe   Haushaltshilfe     Home help          Inside work
 Heimpflege       Heimpflege         Home care          Inside work
 Büro             Bureau             Office             Office work
================ ================== ================== =====================
<BLANKLINE>
