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

Presto uses the :mod:`lino_xl.lib.cal.workflows.voga` workflow, but with some
customizations:

- Add a calendar entry state "missed" (which means that the
  *client* missed the appointment).
- Don't refuse to mark an entry as "took place"
  when a guest (a worker) is still "invited".


>>> rt.show(cal.EntryStates)
====== ============ =============== ============= ================= ======== =================== =========
 Wert   name         Text            Button text   Gäste ausfüllen   Stabil   nicht blockierend   No auto
------ ------------ --------------- ------------- ----------------- -------- ------------------- ---------
 10     suggested    Vorschlag       ?             Ja                Nein     Nein                Nein
 20     draft        Geplant         ☐             Ja                Nein     Nein                Nein
 50     took_place   Stattgefunden   ☑             Nein              Ja       Nein                Nein
 60     missed       Verpasst        ☉             Nein              Ja       Nein                Ja
 70     cancelled    Abgesagt        ⚕             Nein              Ja       Ja                  Ja
====== ============ =============== ============= ================= ======== =================== =========
<BLANKLINE>


Don't refuse to mark an entry as "took place" when a guest (a worker) is still
"invited". The internal name of the default guest state is "invited", but that's
only the internal name, the verbose name is "Present".   Saying that a
deployment took place, in Presto means that you confirm that all invited workers
were present.

>>> rt.show(cal.GuestStates)
====== ========= ============== ================= =============
 Wert   name      Nachträglich   Text              Button text
------ --------- -------------- ----------------- -------------
 10     invited   Nein           Anwesend          ☑
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
============ ============ ============== ============================================================= ============================================== ===========
 Beginnt am   Beginnt um   Arbeiter       Kalendereintrag                                               Workflow                                       Bemerkung
------------ ------------ -------------- ------------------------------------------------------------- ---------------------------------------------- -----------
 16.03.17     14:00:00     Frau Helen     `JACOBS Jacqueline (136) Eupen Einsatz 2  <Detail>`__         **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 21.03.17     11:00:00     Frau Maria     `MALMENDIER Marc (145) Eupen Einsatz 4  <Detail>`__           **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 23.03.17     13:00:00     Herr Ahmed     `RADERMECKER Rik (172) Amsterdam Einsatz 4  <Detail>`__       **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 15.04.17     11:00:00     Frau Maria     `LAHM Lisa (175) Aachen Einsatz 6  <Detail>`__                **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 06.05.17     11:00:00     Herr Conrad    `EVERTZ Bernd (125) Eupen Einsatz 11  <Detail>`__             **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 30.05.17     11:00:00     Herr Conrad    `EMONTS-GAST Erna (151) Raeren Einsatz 13  <Detail>`__        **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 26.06.17     11:00:00     Frau Maria     `HILGERS Hildegard (132) Eupen Deployment 5  <Detail>`__      **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 22.07.17     08:00:00     Herr Garry     `DERICUM Daniel (120) Eupen Einsatz 22  <Detail>`__           **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 29.07.17     09:00:00     Frau Evelyne   `MIESSEN Michael (147) Eupen Einsatz 22  <Detail>`__          **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 16.08.17     08:00:00     Herr Garry     `CHANTRAINE Marc (119) Eupen Einsatz 24  <Detail>`__          **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 19.08.17     09:00:00     Frau Evelyne   `LEFFIN Josefine (144) Eupen Einsatz 24  <Detail>`__          **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 23.08.17     14:00:00     Frau Helen     `JOUSTEN Jan (139) Eupen Einsatz 26  <Detail>`__              **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 09.09.17     11:00:00     Frau Maria     `EVERTZ Bernd (125) Eupen Deployment 7  <Detail>`__           **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 09.09.17     14:00:00     Frau Helen     `JACOBS Jacqueline (136) Eupen Einsatz 27  <Detail>`__        **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 26.04.18     08:00:00     Herr Dennis    `EMONTS Daniel (127) Eupen Deployment 15  <Detail>`__         **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 03.06.18     09:00:00     Frau Beata     `RADERMACHER Edgard (156) Raeren Deployment 16  <Detail>`__   **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 06.07.18     08:00:00     Herr Dennis    `DERICUM Daniel (120) Eupen Deployment 17  <Detail>`__        **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
 13.08.18     09:00:00     Frau Beata     `MIESSEN Michael (147) Eupen Deployment 18  <Detail>`__       **⚕ Sucht Ersatz** → [Ersatz suchen] [☑] [☉]
============ ============ ============== ============================================================= ============================================== ===========
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
 Umzüge           Umzüge             Moves              Craftsmen
 Renovierung      Renovierung        Renovation         Craftsmen
 Haushaltshilfe   Haushaltshilfe     Home help          Home care
 Heimpflege       Heimpflege         Home care          Home care
 Büro             Bureau             Office             Office work
================ ================== ================== =====================
<BLANKLINE>
